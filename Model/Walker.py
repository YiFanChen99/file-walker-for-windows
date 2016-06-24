# -*- coding: utf-8 -*-
import os
from ModelUtility.Settings import IGNORED_DIR_PREFIX, IGNORED_EXTENSION
from ModelUtility.Filename import Filename


def walk_and_call_action(the_operator, path):
    for dirpath, dirnames, filenames in os.walk(path):
        drop_ignored_dir(dirnames)
        for filename in filenames:
            if not is_ignored_file(filename):
                the_operator.action(dirpath, Filename(filename))


def drop_ignored_dir(dirnames):
    """ Remove dir that should be ignored from list. """
    dirnames[:] = [dirname for dirname in dirnames if not is_ignored_dir(dirname)]


def is_ignored_dir(dirname):
    """ Check whether dirname start with IGNORED_DIR_PREFIX. """
    return any(prefix for prefix in IGNORED_DIR_PREFIX if dirname.startswith(prefix))


def is_ignored_file(filename):
    """ Check whether filename has extension in IGNORED_EXTENSION. """
    return Filename(filename).extension in IGNORED_EXTENSION
