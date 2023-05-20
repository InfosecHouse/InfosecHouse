# -*- coding: utf-8 -*-
"""
    readtime.compat
    ~~~~~~~~~~~~~~~

    For working with Python2 and Python3.

    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import sys


IS_PY2 = sys.version_info[0] == 2


if IS_PY2:  # pragma: nocover

    def u(text):
        if text is None:
            return None
        try:
            return text.decode('utf-8')
        except:
            try:
                return text.decode(sys.getdefaultencoding())
            except:
                try:
                    return unicode(text)
                except:
                    return text

else:  # pragma: nocover

    def u(text):
        if text is None:
            return None
        if isinstance(text, bytes):
            try:
                return text.decode('utf-8')
            except:
                try:
                    return text.decode(sys.getdefaultencoding())
                except:
                    pass
        try:
            return str(text)
        except:
            return text
