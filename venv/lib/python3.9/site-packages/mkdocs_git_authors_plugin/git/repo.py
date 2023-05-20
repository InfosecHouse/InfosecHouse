from pathlib import Path
from .command import GitCommand


class Repo(object):
    """
    Abstraction of a Git repository (i.e. the MkDocs project).
    """

    def __init__(self):
        self._root = self.find_repo_root()
        self._total_lines = 0

        # Store Commit, indexed by 40 char SHA
        self._commits = {}
        # Store Page objects, indexed by Path object
        self._pages = {}
        # Store Author objects, indexed by email
        self._authors = {}

    def add_total_lines(self, cnt: int = 1):
        """
        Add line(s) to the number of total lines in the repository.

        Args:
            number of lines to add, default: 1
        """
        self._total_lines += cnt

    def author(self, name, email: str):
        """Return an Author object identified by name and email.

        Note: authors are indexed by their email only.
        If no Author object has yet been registered
        a new one is created using name and email.

        Args:
            name: author's full name
            email: author's email address.

        Returns:
            Author object
        """
        if not self._authors.get(email, None):
            from .author import Author

            self._authors[email] = Author(self, name, email)
        return self._authors[email]

    def get_authors(self):
        """
        Sorted list of authors in the repository.

        Default sort order is by ascending names, 
        and decending when contribution or line count is shown

        Args:

        Returns:
            List of Author objects
        """
        reverse = self.config("show_line_count") or self.config("show_contribution")

        return sorted(
            [author for author in self._authors.values()],
            key=self._sort_key,
            reverse=reverse,
        )

    def config(self, key: str = ""):
        """
        Return the plugin configuration dictionary or a single config value.

        Args:
            key: lookup key or an empty string.
        """
        return self._config.get(key) if key else self._config

    def find_repo_root(self):
        """
        Determine the root directory of the Git repository,
        in case the current working directory is different from that.

        Raises a GitCommandError if we're not in a Git repository
        (or Git is not installed).

        Args:

        Returns:
            path as a string
        """
        cmd = GitCommand("rev-parse", ["--show-toplevel"])
        cmd.run()
        return cmd.stdout()[0]

    def get_commit(self, sha: str, **kwargs):
        """
        Return the (cached) Commit object for given sha.

        Implicitly creates a new Commit object upon first request,
        which will trigger the git show processing.

        Args:
            40-byte SHA string

        Returns:
            Commit object
        """
        if not self._commits.get(sha):
            from .commit import Commit

            self._commits[sha] = Commit(self, sha, **kwargs)
        return self._commits.get(sha)

    def page(self, path):
        """
        Return the (cached) Page object for given path.

        Implicitly creates a new Page object upon first request,
        which will trigger the git blame processing.

        Args:
            path: path (str or Path) to the page's markdown source.

        Returns:
            Page object
        """
        if type(path) == str:
            path = Path(path)
        if not self._pages.get(path):
            from .page import Page

            self._pages[path] = Page(self, path)
        return self._pages[path]

    def set_config(self, plugin_config):
        """
        Store the plugin configuration in the Repo instance.

        Args:
            - plugin_config: dictionary
        """
        self._config = plugin_config

    def _sort_key(self, author):
        """
        Return a sort key for an author.

        Args:
            author: an Author object

        Returns:
            comparison key for the sorted() function,
        """
        if self.config("show_line_count") or self.config("show_contribution") or self.config("sort_authors_by") == "contribution":
            key = "contribution"
        else:
            key = "name"

        func = getattr(author, key)
        return func()

    def total_lines(self):
        """
        The total number of lines in the project's markdown files
        (as counted through git blame).

        Args:

        Returns:
            int total number of lines in the project's markdown files
        """
        return self._total_lines


class AbstractRepoObject(object):
    """
    Base class for objects that live with a repository context.
    """

    def __init__(self, repo: Repo):
        self._repo = repo

    def repo(self):
        """
        Return a reference to the Repo object.

        Args:

        Returns:
            Repo instance
        """
        return self._repo
