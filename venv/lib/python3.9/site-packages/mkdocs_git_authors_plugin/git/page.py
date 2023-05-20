from pathlib import Path
import re
import logging
from .repo import Repo, AbstractRepoObject
from .command import GitCommand, GitCommandError

logger = logging.getLogger("mkdocs.plugins")


class Page(AbstractRepoObject):
    """
    Results of git blame for a given file.

    Stores a list of tuples with a reference to a
    Commit object and a list of consecutive lines
    modified by that commit.
    """

    def __init__(self, repo: Repo, path: Path):
        """
        Instantiate a Page object

        Args:
            repo: Reference to the global Repo instance
            path: Absolute path to the page's Markdown file
        """
        super().__init__(repo)
        self._path = path
        self._sorted = False
        self._total_lines = 0
        self._authors = []
        try:
            self._process_git_blame()
        except GitCommandError:
            logger.warning(
                "[git-authors-plugin] %s has not been committed yet. Lines are not counted"
                % path
            )

    def add_total_lines(self, cnt: int = 1):
        """
        Add line(s) to the count of total lines for the page.

        Arg:
            cnt: number of lines to add. Default: 1
        """
        self._total_lines += cnt

    def get_authors(self):
        """
        Return a sorted list of authors for the page

        The list is sorted once upon first request.
        Sorting is done by author name or contribution.

        Args:

        Returns:
            sorted list with Author objects
        """
        if not self._sorted:
            repo = self.repo()
            reverse = repo.config("show_line_count") or repo.config("show_contribution") or repo.config("sort_authors_by") == "contribution"
            self._authors = sorted(self._authors, key=repo._sort_key, reverse=reverse)
            self._sorted = True
            author_threshold = repo.config("authorship_threshold_percent")
            if author_threshold > 0 and len(self._authors) > 1:
                self._authors = [a for a in self._authors if a.contribution()*100 > author_threshold]
        return self._authors

    def _process_git_blame(self):
        """
        Execute git blame and parse the results.

        This retrieves all data we need, also for the Commit object.
        Each line will be associated with a Commit object and counted
        to its author's "account".
        Whether empty lines are counted is determined by the
        count_empty_lines configuration option.

        git blame --porcelain will produce output like the following
        for each line in a file:

        When a commit is first seen in that file:
            30ed8daf1c48e4a7302de23b6ed262ab13122d31 1 2 1
            author John Doe
            author-mail <j.doe@example.com>
            author-time 1580742131
            author-tz +0100
            committer John Doe
            committer-mail <j.doe@example.com>
            committer-time 1580742131
            summary Fancy commit message title
            filename home/docs/README.md
                    line content (indicated by TAB. May be empty after that)

        When a commit has already been seen *in that file*:
            82a3e5021b7131e31fc5b110194a77ebee907955 4 5
                    line content

        In this case the metadata is not repeated, but it is guaranteed that
        a Commit object with that SHA has already been created so we don't
        need that information anymore.

        When a line has not been committed yet:
            0000000000000000000000000000000000000000 1 1 1
            author Not Committed Yet
            author-mail <not.committed.yet>
            author-time 1583342617
            author-tz +0100
            committer Not Committed Yet
            committer-mail <not.committed.yet>
            committer-time 1583342617
            committer-tz +0100
            summary Version of books/main/docs/index.md from books/main/docs/index.md
            previous 1f0c3455841488fe0f010e5f56226026b5c5d0b3 books/main/docs/index.md
            filename books/main/docs/index.md
                    uncommitted line content

        In this case exactly one Commit object with the special SHA and fake
        author will be created and counted.

        Args:
            ---
        Returns:
            --- (this method works through side effects)
        """

        re_sha = re.compile(r"^\w{40}")

        cmd = GitCommand("blame", ["--porcelain", str(self._path)])
        cmd.run()

        lines = cmd.stdout()

        # in case of empty, non-committed files, raise error
        if len(lines) == 0:
            raise GitCommandError

        commit_data = {}
        for line in lines:
            key = line.split(" ")[0]
            m = re_sha.match(key)
            if m:
                commit_data = {"sha": key}
            elif key in [
                "author",
                "author-mail",
                "author-time",
                "author-tz",
                "summary",
            ]:
                commit_data[key] = line[len(key) + 1 :]
            elif line.startswith("\t"):
                # assign the line to a commit
                # and create the Commit object if necessary
                commit = self.repo().get_commit(
                    commit_data.get("sha"),
                    # The following values are guaranteed to be present
                    # when a commit is seen for the first time,
                    # so they can be used for creating a Commit object.
                    author_name=commit_data.get("author"),
                    author_email=commit_data.get("author-mail"),
                    author_time=commit_data.get("author-time"),
                    author_tz=commit_data.get("author-tz"),
                    summary=commit_data.get("summary"),
                )
                if len(line) > 1 or self.repo().config("count_empty_lines"):
                    author = commit.author()
                    if author not in self._authors:
                        self._authors.append(author)
                    author.add_lines(self, commit)
                    self.add_total_lines()
                    self.repo().add_total_lines()

    def path(self):
        """
        The path to the markdown file.

        Args:

        Returns:
            Absolute path as Path object.
        """
        return self._path

    def total_lines(self):
        """
        Total number of lines in the markdown source file.

        Args:

        Returns:
            int
        """
        return self._total_lines
