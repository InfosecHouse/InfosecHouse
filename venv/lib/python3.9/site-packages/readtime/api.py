# -*- coding: utf-8 -*-
"""
    readtime.api
    ~~~~~~~~~~~~

    Contains public methods.

    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


from . import utils


def of_text(text, wpm=None):
    """Get the read time of some text.

    :param text:  String of text (Assumes utf-8).
    """

    return utils.read_time(text, format='text', wpm=wpm)


def of_html(html, wpm=None):
    """Get the read time of some HTML.

    :param html:  String of HTML.
    """

    return utils.read_time(html, format='html', wpm=wpm)


def of_markdown(markdown, wpm=None):
    """Get the read time of some Markdown.

    :param markdown:  String of Markdown.
    """

    return utils.read_time(markdown, format='markdown', wpm=wpm)
