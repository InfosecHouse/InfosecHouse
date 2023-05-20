# -*- coding: utf-8 -*-
"""
    readtime.result
    ~~~~~~~~~~~~~~~

    For returning read time results.

    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


from __future__ import division

import math
import operator
from datetime import timedelta

from ._compat import u, IS_PY2


class Result(object):
    delta = None

    def __init__(self, seconds=None, wpm=None):
        self.wpm = wpm
        self.delta = timedelta(seconds=seconds)
        self._add_operator_methods()

    def __repr__(self):
        return u(self.text + ' read')

    def __unicode__(self):
        return self.__repr__()  # pragma: nocover

    def __str__(self):
        if IS_PY2:
            return self.__repr__().encode('utf-8')
        else:
            return self.__repr__()

    @property
    def seconds(self):
        return int(self.total_seconds(self.delta))

    @property
    def minutes(self):
        minutes = int(math.ceil(self.seconds / 60))
        if minutes < 1:  # Medium's formula has a minimum of 1 min read time
            minutes = 1
        return minutes

    @property
    def text(self):
        return u('{minutes} min').format(minutes=self.minutes)

    def total_seconds(self, delta):
        """timedelta.total_seconds for Python2.6 compatibility."""

        return ((delta.microseconds + (delta.seconds + delta.days * 24 * 3600) * 1e6) / 1e6)

    def _add_operator_methods(self):
        for op in dir(operator):
            can_set = (getattr(self.__class__, op, None) is None and
                       getattr(self.delta, op, None) is not None and
                       op.startswith('__') and
                       op.endswith('__'))
            if can_set:
                try:
                    setattr(self.__class__, op, self._create_method(op))
                except (AttributeError, TypeError):
                    pass

    def _create_method(self, op):
        fn = getattr(self.delta, op)

        def method(cls, other, *args, **kwargs):
            delta = fn(other.delta)
            return Result(seconds=self.total_seconds(delta), wpm=self.wpm)

        return method
