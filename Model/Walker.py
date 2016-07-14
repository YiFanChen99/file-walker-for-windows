# -*- coding: utf-8 -*-
import os
from ModelUtility.Settings import IGNORED_DIR_PREFIX, IGNORED_EXTENSION, FILE_PROCESS_LOG, IS_LOG_IGNORED_DIR, IS_LOG_IGNORED_FILE
from ModelUtility.Filename import Filename
from Model.Logger import Logger


class Walker(object):
    def __init__(self, file_log=FILE_PROCESS_LOG):
        self.logger = Logger(file_log)

    def walk_and_call_action(self, the_operator, path):
        for dirpath, dirnames, filenames in os.walk(path):
            self.drop_ignored_dir(dirnames)
            for filename in filenames:
                if not self.is_ignored_file(filename):
                    the_operator.action(dirpath, Filename(filename))
                    self.logger.add_acted_file(dirpath, filename)
                else:
                    self.logger.add_ignored_file(dirpath, filename)
        self.logger.export(the_operator, IS_LOG_IGNORED_DIR, IS_LOG_IGNORED_FILE)

    def drop_ignored_dir(self, dirnames):
        """ Remove dir that should be ignored from list. """
        dirnames[:] = [dirname for dirname in dirnames if not self.is_ignored_dir(dirname)]

    def is_ignored_dir(self, dirname):
        """ Check whether dirname start with IGNORED_DIR_PREFIX. """
        is_ignored = any(prefix for prefix in IGNORED_DIR_PREFIX if dirname.startswith(prefix))
        if is_ignored:
            self.logger.add_ignored_dir(dirname)
        return is_ignored

    @staticmethod
    def is_ignored_file(filename):
        """ Check whether filename has extension in IGNORED_EXTENSION. """
        return Filename(filename).extension in IGNORED_EXTENSION
