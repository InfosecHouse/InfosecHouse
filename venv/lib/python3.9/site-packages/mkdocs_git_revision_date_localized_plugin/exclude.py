"""
Module to assist exclude certain files being processed by plugin.

Inspired by https://github.com/apenwarr/mkdocs-exclude
"""
import os
import fnmatch
from typing import List


def exclude(src_path: str, globs: List[str]) -> bool:
    """
    Determine if a src_path should be excluded.

    Supports globs (e.g. folder/* or *.md).
    Credits: code inspired by / adapted from
    https://github.com/apenwarr/mkdocs-exclude/blob/master/mkdocs_exclude/plugin.py

    Args:
        src_path (src): Path of file
        globs (list): list of globs
    Returns:
        (bool): whether src_path should be excluded
    """
    assert isinstance(src_path, str)
    assert isinstance(globs, list)

    for g in globs:
        if fnmatch.fnmatchcase(src_path, g):
            return True

        # Windows reports filenames as eg.  a\\b\\c instead of a/b/c.
        # To make the same globs/regexes match filenames on Windows and
        # other OSes, let's try matching against converted filenames.
        # On the other hand, Unix actually allows filenames to contain
        # literal \\ characters (although it is rare), so we won't
        # always convert them.  We only convert if os.sep reports
        # something unusual.  Conversely, some future mkdocs might
        # report Windows filenames using / separators regardless of
        # os.sep, so we *always* test with / above.
        if os.sep != "/":
            src_path_fix = src_path.replace(os.sep, "/")
            if fnmatch.fnmatchcase(src_path_fix, g):
                return True

    return False
