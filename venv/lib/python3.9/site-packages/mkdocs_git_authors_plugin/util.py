from datetime import datetime, timezone, timedelta
from pathlib import Path


def commit_datetime(author_time: str, author_tz: str):
    """
    Convert a commit's timestamp to an aware datetime object.

    Args:
        author_time: Unix timestamp string
        author_tz: string in the format +hhmm

    Returns:
        datetime.datetime object with tzinfo
    """

    # timezone info looks like +hhmm or -hhmm
    tz_hours = int(author_tz[:3])
    th_minutes = int(author_tz[0] + author_tz[3:])

    return datetime.fromtimestamp(
        int(author_time), timezone(timedelta(hours=tz_hours, minutes=th_minutes))
    )


def commit_datetime_string(dt: datetime):
    """
    Return a string representation for a commit's timestamp.

    Args:
        dt: datetime object with tzinfo

    Returns:
        string representation (should be localized)
    """
    return dt.strftime("%c %z")


def page_authors_summary(page, config: dict):
    """
    A summary of the authors' contributions on a page level
    
    Args:
        page (Page): Page class
        config (dict): plugin's config dict
    
    Returns:
        str: HTML text with authors
    """

    authors = page.get_authors()
    authors_summary = []
    author_name = ""

    for author in authors:
        contrib = (
            " (%s)" % author.contribution(page.path(), str)
            if page.repo().config("show_contribution") and len(page.get_authors()) > 1
            else ""
        )
        if page.repo().config("show_email_address"):
            author_name = "<a href='mailto:%s'>%s</a>" % (author.email(), author.name())
        else:
            author_name = author.name()
        authors_summary.append("%s%s" % (author_name, contrib))

    authors_summary = ", ".join(authors_summary)
    return "<span class='git-page-authors git-authors'>%s</span>" % authors_summary


def site_authors_summary(authors, config: dict):
    """
    A summary list of the authors' contributions on repo level.

    Iterates over all authors and produces an HTML <ul> list with
    their names and overall contribution details (lines/percentage).

    TODO:
    - The output should be configurable or at least localizable
        (suggestions:
        - load a template with named fields for the values
            (user may provide alternative template)
        - provide plugin configuration options for the various labels
        )

    Args:
        authors: sorted list of Author objects
        config: plugin's config dict

    Returns:
        Unordered HTML list as a string.
    """
    show_contribution = config["show_contribution"]
    show_line_count = config["show_line_count"]
    show_email_address = config["show_email_address"]

    result = """
<span class='git-authors'>
    <ul>
        """
    for author in authors:
        contribution = (
            " (%s)" % author.contribution(None, str) if show_contribution else ""
        )
        lines = ": %s lines" % author.lines() if show_line_count else ""
        author_name = ""
        if show_email_address:
            author_name = '<a href="mailto:%s">%s</a>' % (author.email(), author.name())
        else:
            author_name = author.name()
        result += """
    <li>{author_name}{lines}{contribution}</li>
    """.format(
            author_name=author_name,
            lines=lines,
            contribution=contribution,
        )
    result += """
    </span>
</ul>
    """
    return result


def page_authors(authors, path):
    """List of dicts with info on page authors
    # TODO: rename to something more representative like 'authors_to_dict()' 
    Args:
        authors (list): list with Author classes
        path (str): path to page
    """
    if type(path) == str:
        path = Path(path)
    return [
        {
            "name": author.name(),
            "email": author.email(),
            "last_datetime": author.datetime(path, str),
            "lines": author.lines(path),
            "lines_all_pages": author.lines(),
            "contribution": author.contribution(path, str),
            "contribution_all_pages": author.contribution(None, str),
        }
        for author in authors
    ]
