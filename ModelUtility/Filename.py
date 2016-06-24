# -*- coding: utf-8 -*-
import os


class Filename(object):
    def __init__(self, name):
        self.name = name

    @property
    def simple_name(self):
        if not hasattr(self, '_simple_name'):
            self.spilt_name()

        return self._simple_name

    @property
    def extension(self):
        if not hasattr(self, '_extension'):
            self.spilt_name()

        return self._extension

    # noinspection PyAttributeOutsideInit
    def spilt_name(self):
        partial_names = os.path.splitext(self.name)
        self._simple_name = partial_names[0]
        self._extension = partial_names[1]
