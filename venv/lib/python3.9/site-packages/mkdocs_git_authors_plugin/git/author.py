from .repo import AbstractRepoObject, Repo
from .page import Page
from .commit import Commit


class Author(AbstractRepoObject):
    """
    Abstraction of an author in the Git repository.
    """

    def __init__(self, repo: Repo, name: str, email: str):
        """
        Instantiate an Author.

        Args:
            repo: reference to the global Repo instance
            name: author's full name
            email: author's email
        """
        super().__init__(repo)
        self._name = name
        self._email = email
        self._pages = {}

    def add_lines(self, page: Page, commit: Commit, lines: int = 1):
        """
        Add line(s) in a given page/commit to the author's data.

        Args:
            page: Page object referencing the markdown file
            commit: commit in which the line was edited (=> timestamp)
            lines: number of lines to add. Default: 1
        """
        path = page.path()
        entry = self.page(path, page)
        entry["lines"] += lines
        current_dt = entry.get("datetime")
        commit_dt = commit.datetime()
        if not current_dt or commit_dt > current_dt:
            entry["datetime"] = commit_dt
            entry["datetime_str"] = commit.datetime(str)

    def contribution(self, path=None, _type=float):
        """
        The author's relative contribution to a page or the repository.

        The result is a number between 0 and 1, optionally formatted to percent

        Args:
            path: path to a file or None (default)
                if a path is given the author's contribution to *this* page
                is calculated, otherwise to the whole repository.
            _type: 'float' (default) or 'str'
                if _type refers to the str type the result is a formatted
                string, otherwise the raw floating point number.

        Returns:
            formatted string or floating point number
        """
        lines = self.lines(path)
        total_lines = (
            self.page(path)["page"].total_lines() if path else self.repo().total_lines()
        )

        # Some pages are empty, that case contribution is 0 by default
        if total_lines == 0:
            result = 0
        else:
            result = lines / total_lines

        if _type == float:
            return result
        else:
            return str(round(result * 100, 2)) + "%"

    def datetime(self, path, fmt=str):
        """
        The author's last modification date for a given page.

        Args:
            path: path (str or Path) to a page
            fmt: str (default) or anything

        Returns:
            a formatted string (fmt=str)
            or a datetime.datetime object with tzinfo
        """
        key = "datetime_str" if fmt == str else "datetime"
        return self.page(path).get(key)

    def email(self):
        """
        The author's email address

        Args:

        Returns:
            email address as string
        """
        return self._email

    def lines(self, path=None):
        """
        The author's total number of lines on a page or in the repository.

        Args:
            path: path (str or Page) to a markdown file, or None (default)

        Returns:
            number of lines (int) in the repository (path=None)
            or on the given page.
        """
        if path:
            return self.page(path)["lines"]
        else:
            return sum([v["lines"] for v in self._pages.values()])

    def name(self):
        """
        The author's full name

        Args:

        Returns:
            The full name as a string.
        """
        return self._name

    def page(self, path, page=None):
        """
        A dictionary with the author's contribution to a page.

        If there is no entry for the given page yet a new one is
        created, optionally using a passed Page object as a fallback
        or creating a new one.

        Args:
            path: path (str or Path) to a page's markdown file
            page: page to use if not already present (default: None)

        Returns:
            dict, indexed by path:
            - page: reference to a (new) Page object
            - lines: author's number of lines in the page
            [
            - datetime
            - datetime_str
            ]: information about the latest modification of the page
            by the author. Will not be present in the freshly instantiated
            entry.
        """
        if not self._pages.get(path):
            self._pages[path] = {
                "page": page or self.repo().page(path),
                "lines": 0
                # datetime and datetime_str will be populated later
            }
        return self._pages[path]
