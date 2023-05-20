"""
MkDocs Plugin.

https://www.mkdocs.org/
https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/
"""
# standard lib
import logging
import re
import os
import time

# 3rd party
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Page
from mkdocs.utils import copy_file
from mkdocs.exceptions import ConfigurationError

# package modules
from mkdocs_git_revision_date_localized_plugin.util import Util
from mkdocs_git_revision_date_localized_plugin.exclude import exclude

from typing import Any, Dict
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))


class GitRevisionDateLocalizedPlugin(BasePlugin):
    """
    Mkdocs plugin to add revision date from Git.

    See https://www.mkdocs.org/user-guide/plugins
    """

    config_scheme = (
        ("fallback_to_build_date", config_options.Type(bool, default=False)),
        ("locale", config_options.Type(str, default=None)),
        ("type", config_options.Type(str, default="date")),
        ("custom_format", config_options.Type(str, default="%d. %B %Y")),
        ("timezone", config_options.Type(str, default="UTC")),
        ("exclude", config_options.Type(list, default=[])),
        ("enable_creation_date", config_options.Type(bool, default=False)),
        ("enabled", config_options.Type(bool, default=True)),
        ("strict", config_options.Type(bool, default=True)),
    )

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        """
        Determine which locale to use.

        The config event is the first event called on build and
        is run immediately after the user configuration is loaded and validated.
        Any alterations to the config should be made here.
        https://www.mkdocs.org/user-guide/plugins/#on_config

        Args:
            config (dict): global configuration object

        Returns:
            dict: global configuration object
        """
        if not self.config.get('enabled'):
            return config
        
        assert self.config['type'] in ["date","datetime","iso_date","iso_datetime","timeago","custom"]

        self.util = Util(config=self.config)

        # Save last commit timestamp for entire site
        self.last_site_revision_timestamp = self.util.get_git_commit_timestamp(
            config.get('docs_dir')
        )

        # Get locale from plugin configuration
        plugin_locale = self.config.get("locale", None)

        # theme locale
        if "theme" in config and "locale" in config.get("theme"):
            custom_theme = config.get("theme")
            theme_locale = custom_theme._vars.get("locale")
            logging.debug(
                "Locale '%s' extracted from the custom theme: '%s'"
                % (theme_locale, custom_theme.name)
            )
        elif "theme" in config and "language" in config.get("theme"):
            custom_theme = config.get("theme")
            theme_locale = custom_theme._vars.get("language")
            logging.debug(
                "Locale '%s' extracted from the custom theme: '%s'"
                % (theme_locale, custom_theme.name)
            )

        else:
            theme_locale = None
            logging.debug(
                "No locale found in theme configuration (or no custom theme set)"
            )

        # First prio: plugin locale
        if plugin_locale:
            locale_set = plugin_locale
            logging.debug("Using locale from plugin configuration: %s" % locale_set)
        # Second prio: theme locale
        elif theme_locale:
            locale_set = theme_locale
            logging.debug(
                "Locale not set in plugin. Fallback to theme configuration: %s"
                % locale_set
            )
        # Lastly, fallback is English
        else:
            locale_set = "en"
            logging.debug("No locale set. Fallback to: %s" % locale_set)

        # Validate locale
        locale_set = str(locale_set)
        assert len(locale_set) == 2, "locale must be a 2 letter code, see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"

        # set locale also in plugin configuration
        self.config["locale"] = locale_set

        # Add pointers to support files for timeago.js
        if self.config.get("type") == "timeago":
            config["extra_javascript"] = ["js/timeago_mkdocs_material.js"] + config[
                "extra_javascript"
            ]
            config["extra_javascript"] = ["js/timeago.min.js"] + config[
                "extra_javascript"
            ]
            config["extra_css"] = ["css/timeago.css"] + config["extra_css"]

        # Compatibility with mkdocs-static-i18n
        plugins = [*OrderedDict(config["plugins"])]
        if "i18n" in plugins:
            if plugins.index("git-revision-date-localized") < plugins.index("i18n"):
                msg = "[git-revision-date-localized] should be defined after the i18n plugin in your mkdocs.yml file. "
                msg += "This is because i18n adds a 'locale' variable to markdown pages that this plugin supports."
                raise ConfigurationError(msg)
        
        return config

    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        """
        Replace jinja2 tags in markdown and templates with the localized dates.

        The page_markdown event is called after the page's markdown is loaded
        from file and can be used to alter the Markdown source text.
        The meta- data has been stripped off and is available as page.meta
        at this point.

        https://www.mkdocs.org/user-guide/plugins/#on_page_markdown

        Args:
            markdown (str): Markdown source text of page as string
            page: mkdocs.nav.Page instance
            config: global configuration object
            site_navigation: global navigation object

        Returns:
            str: Markdown source text of page as string
        """
        if not self.config.get('enabled'):
            return markdown

        # Exclude pages specified in config
        excluded_pages = self.config.get("exclude", [])
        if exclude(page.file.src_path, excluded_pages):
            logging.debug("Excluding page " + page.file.src_path)
            return markdown

        # Find the locale

        # First prio is use mkdocs-static-i18n locale if set
        try:
            locale = page.locale

        except AttributeError:
            locale = None

        # Second prio is a frontmatter variable 'locale' set in the markdown
        if not locale:
            if "locale" in page.meta:
                locale = page.meta['locale']

        # Finally, if no page locale set, we take the locale determined on_config()
        if not locale:
            locale = self.config.get("locale")
        
        # MkDocs supports 2-letter and 5-letter locales
        # https://www.mkdocs.org/user-guide/localizing-your-theme/#supported-locales
        # We need the 2 letter variant
        if len(locale) == 5:
            locale = locale[:2]
        assert len(locale) == 2, "locale must be a 2 letter code, see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"
        
        # Retrieve git commit timestamp
        # Except for generated pages (f.e. by mkdocs-gen-files plugin)
        if hasattr(page.file, "generated_by"):
            last_revision_timestamp = int(time.time())
        else:
            last_revision_timestamp = self.util.get_git_commit_timestamp(
                    path=page.file.abs_src_path,
                    is_first_commit=False,
            )

        # Last revision date
        revision_dates = self.util.get_date_formats_for_timestamp(last_revision_timestamp, locale=locale, add_spans=True)
        revision_date = revision_dates[self.config["type"]]

        # timeago output is dynamic, which breaks when you print a page
        # This ensures fallback to type "iso_date"
        # controlled via CSS (see on_post_build() event)
        if self.config["type"] == "timeago":
            revision_date += revision_dates["iso_date"]

        # Add to page meta information, for developers
        # Include variants without the CSS <span> elements (raw date strings)
        page.meta["git_revision_date_localized"] = revision_date
        revision_dates_raw = self.util.get_date_formats_for_timestamp(last_revision_timestamp, locale=locale, add_spans=False)
        for date_type, date_string in revision_dates_raw.items():
            page.meta["git_revision_date_localized_raw_%s" % date_type] = date_string

        # Replace any occurances in markdown page
        markdown = re.sub(
            r"\{\{\s*git_revision_date_localized\s*\}\}",
            revision_date,
            markdown,
            flags=re.IGNORECASE,
        )

        # Also add site last updated information, for developers
        site_dates = self.util.get_date_formats_for_timestamp(self.last_site_revision_timestamp, locale=locale, add_spans=True)
        site_date = site_dates[self.config["type"]]
        if self.config["type"] == "timeago":
            site_date += site_dates["iso_date"]
        page.meta["git_site_revision_date_localized"] = site_date
        site_dates_raw = self.util.get_date_formats_for_timestamp(self.last_site_revision_timestamp, locale=locale, add_spans=False)
        for date_type, date_string in site_dates_raw.items():
            page.meta["git_site_revision_date_localized_raw_%s" % date_type] = date_string

        # Replace any occurances in markdown page
        markdown = re.sub(
            r"\{\{\s*git_site_revision_date_localized\s*\}\}",
            site_date,
            markdown,
            flags=re.IGNORECASE,
        )


        # If creation date not enabled, return markdown
        # This is for speed: prevents another `git log` operation each file
        if not self.config.get("enable_creation_date"):
            return markdown
    
        # Retrieve git commit timestamp
        # Except for generated pages (f.e. by mkdocs-gen-files plugin)
        if hasattr(page.file, "generated_by"):
            first_revision_timestamp = int(time.time())
        else:
            first_revision_timestamp = self.util.get_git_commit_timestamp(
                path=page.file.abs_src_path,
                is_first_commit=True,
            )

        # Creation date formats
        creation_dates = self.util.get_date_formats_for_timestamp(first_revision_timestamp, locale=locale, add_spans=True)
        creation_date = creation_dates[self.config["type"]]

        # timeago output is dynamic, which breaks when you print a page
        # This ensures fallback to type "iso_date"
        # controlled via CSS (see on_post_build() event)
        if self.config["type"] == "timeago":
            creation_date += creation_dates["iso_date"]

        # Add to page meta information, for developers
        # Include variants without the CSS <span> elements (raw date strings)
        page.meta["git_creation_date_localized"] = creation_date
        creation_dates_raw = self.util.get_date_formats_for_timestamp(first_revision_timestamp, locale=locale, add_spans=False)
        for date_type, date_string in creation_dates_raw.items():
            page.meta["git_creation_date_localized_raw_%s" % date_type] = date_string

        # Replace any occurances in markdown page
        markdown = re.sub(
            r"\{\{\s*git_creation_date_localized\s*\}\}",
            creation_date,
            markdown,
            flags=re.IGNORECASE,
        )

        return markdown

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        """
        Run on post build.

        Adds the timeago assets to the build.
        """
        # Add timeago files:
        if self.config.get("type") == "timeago" and self.config.get('enabled'):
            files = [
                "js/timeago.min.js",
                "js/timeago_mkdocs_material.js",
                "css/timeago.css",
            ]
            for file in files:
                dest_file_path = os.path.join(config["site_dir"], file)
                src_file_path = os.path.join(HERE, file)
                assert os.path.exists(src_file_path)
                copy_file(src_file_path, dest_file_path)
