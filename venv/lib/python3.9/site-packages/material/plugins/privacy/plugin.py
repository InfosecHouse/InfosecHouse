# Copyright (c) 2016-2023 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import errno
import logging
import os
import posixpath
import re
import requests
import sys

from colorama import Fore, Style
from concurrent.futures import Future, ThreadPoolExecutor, wait
from fnmatch import fnmatch
from hashlib import sha1
from lxml.html import HtmlElement, fragment_fromstring, tostring
from mkdocs import utils
from mkdocs.commands.build import DuplicateFilter
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, event_priority
from mkdocs.structure.files import File, Files
from re import Match
from urllib.parse import ParseResult as URL, urlparse

from material.plugins.privacy.config import PrivacyConfig

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Privacy plugin
class PrivacyPlugin(BasePlugin[PrivacyConfig]):
    supports_multiple_instances = True

    # Initialize plugin
    def on_config(self, config):
        self.site = urlparse(config.site_url or "")
        if not self.config.enabled:
            return

        # Initialize thread pool
        self.pool = ThreadPoolExecutor(self.config.concurrency)
        self.pool_jobs: list[Future] = []

        # Initialize collections of external assets
        self.assets = Files([])
        self.assets_done: list[File] = []
        self.assets_expr_map = dict({
            ".css": r"url\((\s*http?[^)]+)\)",
            ".js": r"[\"'](http[^\"']+\.(?:css|js(?:on)?))[\"']",
            **self.config.assets_expr_map
        })

    # Process external style sheets and scripts (run latest) - run this hook
    # after all other plugins, so they can add additional assets
    @event_priority(-100)
    def on_files(self, files, *, config):
        if not self.config.enabled:
            return

        # Skip if external assets must not be processed
        if not self.config.assets:
            return

        # Find all external style sheet and script files that are provided as
        # part of the build (= already known to MkDocs on startup)
        for initiator in files.media_files():
            file = None

            # Check if the file has dependent external assets that must be
            # downloaded. Create and enqueue a job for each external asset.
            for url in self._parse_media(initiator):
                if not self._is_excluded(url, initiator):
                    file = self._queue(url, config, concurrent = True)

                    # If site URL is not given, ensure that Mermaid.js is always
                    # present. This is a special case, as Material for MkDocs
                    # automatically loads Mermaid.js when a Mermaid diagram is
                    # found in the page - https://bit.ly/36tZXsA.
                    if "mermaid.min.js" in url.path and not config.site_url:
                        mermaid = url.geturl()
                        if mermaid not in config.extra_javascript:
                            config.extra_javascript.append(mermaid)

            # The local asset references at least one external asset, which
            # means we must download and replace them later
            if file:
                self.assets.append(initiator)
                files.remove(initiator)

        # Process external style sheet and script files, bringing them under
        # our control by adding them to the collection of external assets
        for path in [*config.extra_css, *config.extra_javascript]:
            url = urlparse(path)
            if not self._is_excluded(url):
                self._queue(url, config, concurrent = True)

    # Process external images in page (run latest) - this stage is the earliest
    # we can start processing external images, since images are the most common
    # type of external asset when writing. Thus, we create and enqueue a job for
    # each image we find that checks if the image needs to be downloaded. Also,
    # downloading all external images at this stage, we reconcile all concurrent
    # jobs in the `on_env` hook, which is the stage in which the optimize plugin
    # will evaluate what images can and need to be optimized. This means we can
    # pass external images through the optimization pipeline. Additionally, we
    # run this hook after all other plugins, so we allow them to add additional
    # images to the page content. How cool is that?
    @event_priority(-100)
    def on_page_content(self, html, *, page, config, files):
        if not self.config.enabled:
            return

        # Skip if external assets must not be processed
        if not self.config.assets:
            return

        # Find all external images and download them if not excluded
        for match in re.findall(
            r"<img[^>]+src=['\"]?http[^>]+>",
            html, flags = re.I | re.M
        ):
            encoded = match.encode("unicode_escape")
            el: HtmlElement = fragment_fromstring(encoded)

            # Create and enqueue job to fetch external image
            url = urlparse(el.get("src"))
            if not self._is_excluded(url, page.file):
                self._queue(url, config, concurrent = True)

    # Reconcile jobs and pass external assets to MkDocs (run earlier) - allow
    # other plugins (e.g. optimize plugin) to post-process external assets
    @event_priority(50)
    def on_env(self, env, *, config, files):
        if not self.config.enabled:
            return

        # Reconcile concurrent jobs and clear thread pool, as we will reuse the
        # same thread pool for fetching all remaining external assets
        wait(self.pool_jobs)
        self.pool_jobs.clear()

        # Append all downloaded assets that are not style sheets or scripts to
        # MkDocs's collection of files, making them available to other plugins
        # for further processing. The remaining exteral assets are patched
        # before copying, which is done at the end of the build process.
        for file in self.assets:
            _, extension = posixpath.splitext(file.dest_uri)
            if extension not in [".css", ".js"]:
                self.assets_done.append(file)
                files.append(file)

    # Process external assets in template (run later)
    @event_priority(-50)
    def on_post_template(self, output_content, *, template_name, config):
        if not self.config.enabled:
            return

        # Skip sitemap.xml and other non-HTML files
        if not template_name.endswith(".html"):
            return

        # Parse and replace links to external assets in template
        initiator = File(template_name, config.docs_dir, config.site_dir, False)
        return self._parse_html(output_content, initiator, config)

    # Process external assets in page (run later)
    @event_priority(-50)
    def on_post_page(self, output, *, page, config):
        if not self.config.enabled:
            return

        # Parse and replace links to external assets
        return self._parse_html(output, page.file, config)

    # Reconcile jobs (run earlier) - allow other plugins (e.g. optimize plugin)
    # to process all downloaded assets, which is why we must reconcile here
    @event_priority(50)
    def on_post_build(self, *, config):
        if not self.config.enabled:
            return

        # Reconcile concurrent jobs and clear thread pool, as we will reuse the
        # same thread pool for patching all links to external assets
        wait(self.pool_jobs)
        self.pool_jobs.clear()

        # Spawn concurrent job to patch all links to dependent external asset
        # in all style sheet and script files
        for file in self.assets:
            _, extension = posixpath.splitext(file.dest_uri)
            if extension in [".css", ".js"]:
                self.pool_jobs.append(self.pool.submit(
                    self._patch, file
                ))

            # Otherwise, just copy external asset to output directory, if we
            # haven't handed control to MkDocs in `on_env` before
            elif file not in self.assets_done:
                file.copy_file()

        # Reconcile concurrent jobs for the last time, so the plugins following
        # in the build process always have a consistent state to work with
        wait(self.pool_jobs)
        self.pool.shutdown()

    # -------------------------------------------------------------------------

    # Check if the given URL is external
    def _is_external(self, url: URL):
        hostname = url.hostname or self.site.hostname
        return hostname != self.site.hostname

    # Check if the given URL is excluded
    def _is_excluded(self, url: URL, initiator: File = None):
        if not self._is_external(url):
            return True

        # Skip if external assets must not be processed
        if not self.config.assets:
            return True

        # If initiator is given, format for printing
        via = ""
        if initiator:
            via = "".join([
                Fore.WHITE, Style.DIM,
                f"in {initiator.src_uri}",
                Style.RESET_ALL
            ])

        # Check if URL matches one of the inclusion patterns
        if self.config.assets_include:
            for pattern in self.config.assets_include:
                if fnmatch(self._map_url_to_path(url), pattern):
                    return False

            # File is not included
            log.debug(f"Excluding external file: {url.geturl()} {via}")
            return True

        # Check if URL matches one of the exclusion patterns
        for pattern in self.config.assets_exclude:
            if fnmatch(self._map_url_to_path(url), pattern):
                log.debug(f"Excluding external file: {url.geturl()} {via}")
                return True

        # Print warning if fetching is not enabled
        if not self.config.assets_fetch:
            log.warning(f"External file: {url.geturl()} {via}")
            return True

        # File is not excluded
        return False

    # -------------------------------------------------------------------------

    # Parse and extract all external assets from a media file using a preset
    # regular expression, and return all URLs found.
    def _parse_media(self, initiator: File) -> "list[URL]":
        _, extension = posixpath.splitext(initiator.dest_uri)
        if extension not in self.assets_expr_map:
            return []

        # Find and extract all external asset URLs
        expr = re.compile(self.assets_expr_map[extension], flags = re.I | re.M)
        with open(initiator.abs_src_path, encoding = "utf-8") as f:
            return [urlparse(url) for url in re.findall(expr, f.read())]

    # Parse template or page HTML and find all external links that need to be
    # replaced. Many of the assets should already be downloaded earlier, i.e.,
    # everything that was directly referenced in the document, but there may
    # still exist external assets that were added by third-party plugins.
    def _parse_html(self, output: str, initiator: File, config: MkDocsConfig):

        # Resolve callback
        def resolve(file: File):
            if utils.is_error_template(initiator.src_uri):
                base = urlparse(config.site_url or "/")
                return posixpath.join(base.path, file.url)
            else:
                return file.url_relative_to(initiator)

        # Replace callback
        def replace(match: Match):
            encoded = match.group().encode("unicode_escape")
            el: HtmlElement = fragment_fromstring(encoded)

            # Handle external link
            if self.config.links and el.tag == "a":
                for key, value in self.config.links_attr_map.items():
                    el.set(key, value)

                # Set `rel=noopener` if link opens in a new window
                if self.config.links_noopener:
                    if el.get("target") == "_blank":
                        rel = re.findall(r"\S+", el.get("rel", ""))
                        if "noopener" not in rel:
                            rel.append("noopener")

                        # Set relationships after adding `noopener`
                        el.set("rel", " ".join(rel))

            # Handle external style sheet or preconnect hint
            if el.tag == "link":
                url = urlparse(el.get("href"))
                if not self._is_excluded(url, initiator):
                    rel = el.get("rel", "")

                    # Replace external preconnect hint
                    if rel == "preconnect":
                        return ""

                    # Replace external style sheet or favicon
                    if rel == "stylesheet" or rel == "icon":
                        file = self._queue(url, config)
                        el.set("href", resolve(file))

            # Handle external script or image
            if el.tag == "script" or el.tag == "img":
                url = urlparse(el.get("src"))
                if not self._is_excluded(url, initiator):
                    file = self._queue(url, config)
                    el.set("src", resolve(file))

            # Return void or opening tag as string, strip closing tag
            decoded = tostring(el).decode("unicode_escape")
            if el.tag in void:
                return decoded
            else:
                tail = 3 + len(el.tag)
                return decoded[:-tail]

        # Find and replace all external asset URLs in current page
        return re.sub(
            r"<(?:(?:a|link)[^>]+href|(?:script|img)[^>]+src)=['\"]?http[^>]+>",
            replace, output, flags = re.I | re.M
        )

    # -------------------------------------------------------------------------

    # Enqueue external asset for download, if not already done
    def _queue(self, url: URL, config: MkDocsConfig, concurrent = False):
        path = self._map_url_to_path(url)
        full = posixpath.join(self.config.assets_fetch_dir, path)

        # Try to retrieve existing file
        file = self.assets.get_file_from_path(full)
        if not file:

            # Compute path to external asset, which is sourced from the cache
            # directory, and generate file to register it with MkDocs as soon
            # as it was downloaded. This allows other plugins to apply
            # additional processing.
            file = self._generate_file(path, config)
            file.url = url.geturl()

            # Spawn concurrent job to fetch external asset if the extension is
            # known and the concurrent flag is set. In that case, this function
            # is called in a context where no replacements are carried out, so
            # the caller must only ensure to reconcile the concurrent jobs.
            _, extension = posixpath.splitext(url.path)
            if extension and concurrent:
                self.pool_jobs.append(self.pool.submit(
                    self._fetch, file, config
                ))

            # Fetch external asset synchronously, as it either has no extension
            # or is fetched from a context in which replacements are done
            else:
                self._fetch(file, config)

            # Register external asset as file
            self.assets.append(file)

        # Return file associated with external asset
        return file

    # Fetch external asset referenced through the given file
    def _fetch(self, file: File, config: MkDocsConfig):

        # Check if external asset needs to be downloaded
        if not os.path.isfile(file.abs_src_path) or not self.config.cache:
            path = file.abs_src_path

            # Download external asset
            log.info(f"Downloading external file: {file.url}")
            res = requests.get(file.url, headers = {

                # Set user agent explicitly, so Google Fonts gives us *.woff2
                # files, which according to caniuse.com is the only format we
                # need to download as it covers the entire range of browsers
                # we're officially supporting.
                "User-Agent": " ".join([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "AppleWebKit/537.36 (KHTML, like Gecko)",
                    "Chrome/98.0.4758.102 Safari/537.36"
                ])
            })

            # Compute expected file extension and append if missing
            mime = res.headers["content-type"].split(";")[0]
            extension = extensions.get(mime)
            if extension and not path.endswith(extension):
                path += extension

            # Write contents and create symlink if no extension was present
            utils.write_file(res.content, path)
            if path != file.abs_src_path:

                # Creating symlinks might fail on Windows. Thus, we just print
                # a warning and continue - see https://bit.ly/3xYFzcZ
                try:
                    os.symlink(os.path.basename(path), file.abs_src_path)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        log.warning(
                            f"Couldn't create symbolic link: {file.src_uri}"
                        )

                    # Fall back for when the symlink could not be created. This
                    # means that the plugin will download the original file on
                    # every build, as the content type cannot be resolved from
                    # the file extension.
                    file.abs_src_path = path

        # Resolve destination if file points to a symlink
        _, extension = os.path.splitext(file.abs_src_path)
        if os.path.isfile(file.abs_src_path):
            file.abs_src_path = os.path.realpath(file.abs_src_path)
            _, extension = os.path.splitext(file.abs_src_path)

            # If the symlink could not be created, we already set the correct
            # extension, so we need to make sure not to append it again
            if not file.abs_dest_path.endswith(extension):
                file.src_uri += extension

                # Compute destination file system path
                file.dest_uri += extension
                file.abs_dest_path += extension

        # Compute destination URL
        file.url = file.dest_uri

        # Parse and enqueue dependent external assets
        for url in self._parse_media(file):
            if not self._is_excluded(url, file):
                self._queue(url, config, concurrent = True)

    # Patch all links to external assets in the given file
    def _patch(self, initiator: File):
        with open(initiator.abs_src_path, encoding = "utf-8") as f:

            # Replace callback
            def replace(match: Match):
                value = match.group(1)

                # Map URL to canonical path
                path = self._map_url_to_path(urlparse(value))
                full = posixpath.join(self.config.assets_fetch_dir, path)

                # Try to retrieve existing file
                file = self.assets.get_file_from_path(full)
                if not file:
                    name = os.readlink(os.path.join(self.config.cache_dir, full))
                    full = posixpath.join(posixpath.dirname(full), name)

                    # Try again after resolving symlink
                    file = self.assets.get_file_from_path(full)

                # This can theoretically never happen, as we're sure that we
                # only replace files that we successfully extracted. However,
                # we might have missed several cases, so it's better to throw
                # here than to swallow the error.
                if not file:
                    log.error(
                        "File not found. This is likely a bug in the built-in "
                        "privacy plugin. Please create an issue with a minimal "
                        "reproduction."
                    )
                    sys.exit(1)

                # Create absolute URL for asset in script
                if file.url.endswith(".js"):
                    url = posixpath.join(self.site.geturl(), file.url)

                # Create relative URL for everything else
                else:
                    url = file.url_relative_to(initiator)

                # Switch external asset URL to local path
                return match.group().replace(value, url)

            # Resolve replacement expression according to asset type
            _, extension = posixpath.splitext(initiator.dest_uri)
            expr = re.compile(self.assets_expr_map[extension], re.I | re.M)

            # Resolve links to external assets in file
            utils.write_file(
                expr.sub(replace, f.read()).encode("utf8"),
                initiator.abs_dest_path
            )

    # -------------------------------------------------------------------------

    # Normalize (= canonicalize) path by removing trailing slashes, and ensure
    # that hidden folders (`.` after `/`) are unhidden. Otherwise MkDocs will
    # not consider them being part of the build and refuse to copy them.
    def _map_url_to_path(self, url: URL):
        path = posixpath.normpath(url.path)
        path = re.sub(r"/\.", "/_", path)

        # Compute digest of query string, as some URLs yield different results
        # for different query strings, e.g. https://unsplash.com/random?Coffee
        if url.query:
            name, extension = posixpath.splitext(path)

            # Inject digest after file name and before file extension, as
            # done for style sheet and script files as well
            digest = sha1(url.query.encode("utf-8")).hexdigest()[:8]
            path = f"{name}.{digest}{extension}"

        # Create and return URL without leading double slashes
        url = url._replace(scheme = "", query = "", fragment = "", path = path)
        return url.geturl()[2:]

    # Create a file for the given path
    def _generate_file(self, path: str, config: MkDocsConfig):
        return File(
            posixpath.join(self.config.assets_fetch_dir, path),
            os.path.abspath(self.config.cache_dir),
            config.site_dir,
            False
        )

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())

# Expected file extensions
extensions = dict({
    "application/javascript": ".js",
    "image/avif": ".avif",
    "image/gif": ".gif",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
    "text/javascript": ".js",
    "text/css": ".css"
})

# Tags that are self-closing
void = set([
    "area",                            # Image map areas
    "base",                            # Document base
    "br",                              # Line breaks
    "col",                             # Table columns
    "embed",                           # External content
    "hr",                              # Horizontal rules
    "img",                             # Images
    "input",                           # Input fields
    "link",                            # Links
    "meta",                            # Metadata
    "param",                           # External parameters
    "source",                          # Image source sets
    "track",                           # Text track
    "wbr"                              # Line break opportunities
])
