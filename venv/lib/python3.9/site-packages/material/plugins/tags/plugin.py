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

import logging
import sys

from collections import defaultdict
from mkdocs import utils
from mkdocs.commands.build import DuplicateFilter
from mkdocs.plugins import BasePlugin

# deprecated, but kept for downward compatibility. Use 'material.plugins.tags'
# as an import source instead. This import is removed in the next major version.
from material.plugins.tags import casefold
from material.plugins.tags.config import TagsConfig

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Tags plugin
class TagsPlugin(BasePlugin[TagsConfig]):
    supports_multiple_instances = True

    # Initialize plugin
    def on_config(self, config):
        if not self.config.enabled:
            return

        # Initialize tags
        self.tags_map = defaultdict(list)
        self.tags_type_map = config.extra.get("tags")

        # Initialize tags index pages
        self.tags_file = None
        self.tags_extra_files = []

    # Resolve index pages (and extra files)
    def on_nav(self, nav, *, config, files):
        if not self.config.enabled:
            return

        # Resolve tags index page
        file = self.config.tags_file
        if file:
            self.tags_file = self._get_tags_file(files, file)

        # Resolve extra tags index pages, if given
        for file, _ in self.config.tags_extra_files.items():
            self.tags_extra_files.append(
                self._get_tags_file(files, file)
            )

    # Build and render tags index(es) and link pages
    def on_page_markdown(self, markdown, *, page, config, files):
        if not self.config.enabled:
            return

        # Render tags index page
        if page.file == self.tags_file:
            return self._render_tag_index(markdown, page)

        # Render extra tags index pages
        path = page.file.src_uri
        if page.file in self.tags_extra_files:
            included = self.config.tags_extra_files.get(path)

            # Check if tag identifiers are defined as a list
            if not isinstance(included, list):
                log.error(
                    f"Page '{path}' in 'tags_extra_files' "
                    f"must list tag identifiers as a list."
                )
                sys.exit(1)

            # Render and return page
            return self._render_tag_index(markdown, page, included)

        # Ensure tags are defined as a list
        tags = page.meta.get("tags", [])
        if not isinstance(tags, list):
            log.warning(f"Page '{path}' uses invalid syntax for tags: {tags}")

        # Link page to each tag
        for name in tags:
            if not name or not isinstance(name, (str, int, float, bool)):
                name = name or "(empty)"
                log.warning(f"Page '{path}' includes invalid tag: {name}")
            else:
                self.tags_map[name].append(page)

                # Ensure tag is in (non-empty) allow list
                if self.config.tags_allowed:
                    if name not in self.config.tags_allowed:
                        log.error(
                            f"Page '{path}' includes a mention of tag "
                            f"which is not in allow list: {name}"
                        )
                        sys.exit(1)

    # Inject tags into page (after search and before minification)
    def on_page_context(self, context, *, page, config, nav):
        if not self.config.enabled:
            return

        # Provide tags for page
        if "tags" in page.meta:
            context["tags"] = [
                self._render_tag(name)
                    for name in page.meta["tags"]
                        if name and isinstance(name, (str, int, float, bool))
            ]

    # -------------------------------------------------------------------------

    # Obtain tags file (and extra files)
    def _get_tags_file(self, files, path):
        file = files.get_file_from_path(path)
        if not file:
            log.error(f"Tags file '{path}' does not exist.")
            sys.exit(1)

        # Hack: 2nd pass for tags index page(s)
        files.append(file)
        return file

    # Render tags index
    def _render_tag_index(self, markdown, tags_index, included = None):
        if not "[TAGS]" in markdown:
            markdown += "\n[TAGS]"

        # Filter tags against inclusion list, if given
        tags = []
        if self.tags_type_map and included:
            for name in self.tags_map.keys():
                if self.tags_type_map.get(name) in included:
                    tags.append(name)

        # Replace placeholder in Markdown with rendered tags index
        return markdown.replace("[TAGS]", "\n".join([
            self._render_tag_links(tags_index, name, self.tags_map[name])
                for name in sorted(
                    tags or self.tags_map.keys(),

                    # Allow for custom comparison functions
                    key     = self.config.tags_compare,
                    reverse = self.config.tags_compare_reverse
                )
        ]))

    # Render the given tag and links to all pages with occurrences
    def _render_tag_links(self, tags_index, name, pages):
        classes = ["md-tag"]
        if self.tags_type_map:
            classes.append("md-tag-icon")
            type = self.tags_type_map.get(name)
            if type:
                classes.append(f"md-tag--{type}")

        # Render section for tag and a link to each page
        classes = " ".join(classes)
        content = [f"## <span class=\"{classes}\">{name}</span>", ""]
        for page in pages:
            url = utils.get_relative_url(
                page.file.src_uri,
                tags_index.file.src_uri
            )

            # Render link to page
            title = page.meta.get("title", page.title)
            content.append(f"- [{title}]({url})")

        # Return rendered tag links
        return "\n".join(content)

    # Render the given tag
    def _render_tag(self, name):
        tag = dict(name = name)

        # Add tag type, if given
        if self.tags_type_map:
            tag["type"] = self.tags_type_map.get(name)

        # Add tag URL, if tags index is enabled
        if self.tags_file:
            tag["url"] = "#".join([
                self.tags_file.url,
                self.config.tags_slugify(
                    name, self.config.tags_slugify_separator
                )
            ])

        # Return tag
        return tag

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
