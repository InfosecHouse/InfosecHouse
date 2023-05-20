"""Utility class for mkdocs plugin."""
import logging
import os
import time
from datetime import datetime

from mkdocs_git_revision_date_localized_plugin.ci import raise_ci_warnings

from babel.dates import format_date, get_timezone
from git import (
    Repo,
    Git,
    GitCommandError,
    GitCommandNotFound,
    InvalidGitRepositoryError,
    NoSuchPathError,
)

from typing import Any, Dict

logger = logging.getLogger("mkdocs.plugins")


class Util:
    """Utility class.

    This helps find git and calculate relevant dates.
    """

    def __init__(self, config={}):
        """Initialize utility class."""
        self.config = config
        self.repo_cache = {}

    def _get_repo(self, path: str) -> Git:
        if not os.path.isdir(path):
            path = os.path.dirname(path)

        if path not in self.repo_cache:
            self.repo_cache[path] = Repo(path, search_parent_directories=True).git
            # Checks if user is running builds on CI
            # and raise appropriate warnings
            raise_ci_warnings(self.repo_cache[path])

        return self.repo_cache[path]

    @staticmethod
    def _date_formats(
        unix_timestamp: float, locale: str = "en", time_zone: str = "UTC", custom_format: str = "%d. %B %Y"
    ) -> Dict[str, Any]:
        """
        Calculate different date formats / types.

        Args:
            unix_timestamp (float): A timestamp in seconds since 1970.
            locale (str): Locale code of language to use. Defaults to 'en'.
            time_zone (str): Timezone database name (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
            custom_format (str): strftime format specifier for the 'custom' type

        Returns:
            dict: Different date formats.
        """
        assert time_zone is not None
        assert locale is not None
        
        utc_revision_date = datetime.utcfromtimestamp(int(unix_timestamp))
        loc_revision_date = utc_revision_date.replace(
            tzinfo=get_timezone("UTC")
        ).astimezone(get_timezone(time_zone))

        return {
            "date": format_date(loc_revision_date, format="long", locale=locale),
            "datetime": " ".join(
                [
                    format_date(loc_revision_date, format="long", locale=locale),
                    loc_revision_date.strftime("%H:%M:%S"),
                ]
            ),
            "iso_date": loc_revision_date.strftime("%Y-%m-%d"),
            "iso_datetime": loc_revision_date.strftime("%Y-%m-%d %H:%M:%S"),
            "timeago": '<span class="timeago" datetime="%s" locale="%s"></span>' % (loc_revision_date.isoformat(), locale),
            "custom": loc_revision_date.strftime(custom_format),
        }

    def get_git_commit_timestamp(
            self,
            path: str,
            is_first_commit: bool = False
    ) -> int:
        """
        Get a list of commit dates in unix timestamp, starts with the most recent commit.

        Args:
            is_first_commit (bool): if true, get the timestamp of the first commit,
                                    else, get that of the most recent commit.
            path (str): Location of a markdown file that is part of a Git repository.
            is_first_commit (bool): retrieve commit timestamp when file was created.

        Returns:
            int: commit date in unix timestamp, starts with the most recent commit.
        """
        commit_timestamp = ""

        # Determine the logging level
        # Only log warnings when plugin is set to strict.
        # That way, users turn those into errors using mkdocs build --strict
        if self.config.get('strict'):
            log = logger.warning
        else:
            log = logger.info

        # perform git log operation
        try:
            # Retrieve author date in UNIX format (%at)
            # https://git-scm.com/docs/git-log#Documentation/git-log.txt-ematem
            # https://git-scm.com/docs/git-log#Documentation/git-log.txt---diff-filterACDMRTUXB82308203
            realpath = os.path.realpath(path)
            git = self._get_repo(realpath)

            if is_first_commit:
                # diff_filter="A" will select the commit that created the file
                commit_timestamp = git.log(
                    realpath, date="unix", format="%at", diff_filter="A", no_show_signature=True, follow=True
                )
                # A file can be created multiple times, through a file renamed. 
                # Commits are ordered with most recent commit first
                # Get the oldest commit only
                if commit_timestamp != "":
                    commit_timestamp = commit_timestamp.split()[-1]
            else:
                # Latest commit touching a specific file
                commit_timestamp = git.log(
                    realpath, date="unix", format="%at", n=1, no_show_signature=True
                )
        except (InvalidGitRepositoryError, NoSuchPathError) as err:
            if self.config.get('fallback_to_build_date'):
                log(
                    "[git-revision-date-localized-plugin] Unable to find a git directory and/or git is not installed."
                    " Option 'fallback_to_build_date' set to 'true': Falling back to build date"
                )
                commit_timestamp = time.time()
            else:
                log(
                    "[git-revision-date-localized-plugin] Unable to find a git directory and/or git is not installed."
                    " To ignore this error, set option 'fallback_to_build_date: true'"
                )
                raise err
        except GitCommandError as err:
            if self.config.get('fallback_to_build_date'):
                log(
                    "[git-revision-date-localized-plugin] Unable to read git logs of '%s'. Is git log readable?"
                    " Option 'fallback_to_build_date' set to 'true': Falling back to build date"
                    % path
                )
                commit_timestamp = time.time()
            else:
                logger.error(
                    "[git-revision-date-localized-plugin] Unable to read git logs of '%s'. "
                    " To ignore this error, set option 'fallback_to_build_date: true'"
                    % path
                )
                raise err
        except GitCommandNotFound as err:
            if self.config.get('fallback_to_build_date'):
                log(
                    "[git-revision-date-localized-plugin] Unable to perform command: 'git log'. Is git installed?"
                    " Option 'fallback_to_build_date' set to 'true': Falling back to build date"
                )
                commit_timestamp = time.time()
            else:
                log(
                    "[git-revision-date-localized-plugin] Unable to perform command 'git log'. Is git installed?"
                    " To ignore this error, set option 'fallback_to_build_date: true'"
                )
                raise err

        # create timestamp
        if commit_timestamp == "":
            commit_timestamp = time.time()
            log(
                "[git-revision-date-localized-plugin] '%s' has no git logs, using current timestamp"
                % path
            )

        return int(commit_timestamp)

    def get_date_formats_for_timestamp(
        self,
        commit_timestamp: int,
        locale: str,
        add_spans: bool = True,
    ) -> Dict[str, str]:
        """
        Determine localized date variants for a given timestamp.

        Args:
            commit_timestamp (int): most recent commit date in unix timestamp.
            locale (str, optional): Locale code of language to use. Defaults to 'en'.
            add_spans: Wraps output in <span> elements with unique classes for easy CSS formatting

        Returns:
            dict: Localized date variants.
        """
        date_formats = self._date_formats(
            unix_timestamp=commit_timestamp, 
            time_zone=self.config.get("timezone"),
            locale=locale,
            custom_format=self.config.get('custom_format')
        )
        if add_spans:
            date_formats = self.add_spans(date_formats)

        return date_formats


    @staticmethod
    def add_spans(date_formats: Dict[str, str]) -> Dict[str, str]:
        """
        Wraps the date string in <span> elements with CSS identifiers.
        """
        for date_type, date_string in date_formats.items():
            date_formats[date_type] = (
                '<span class="git-revision-date-localized-plugin git-revision-date-localized-plugin-%s">%s</span>'
                % (date_type, date_string)
            )
        return date_formats
