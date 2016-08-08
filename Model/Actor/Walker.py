# -*- coding: utf-8 -*-
import os
from ModelUtility.Settings import IGNORED_DIR_PREFIX, IGNORED_EXTENSION, FILE_PROCESS_LOG,\
    IS_LOG_IGNORED
from ModelUtility.Filename import Filename
from Model.Logger import Logger


class Walker(object):
    @staticmethod
    def get_id():
        raise Exception('Did not override method get_id.')

    @staticmethod
    def get_description():
        raise Exception('Did not override method get_description.')

    @staticmethod
    def get_config():
        raise Exception('Did not override method get_config.')

    def __init__(self, file_log=FILE_PROCESS_LOG):
        self.logger = Logger(file_log)
        self.ignored_dir_prefix = IGNORED_DIR_PREFIX
        self.ignored_extension = IGNORED_EXTENSION

    def walk_and_action(self, path):
        for dirpath, dirnames, filenames in os.walk(path):
            self.judge_dirnames(dirpath, dirnames)
            self.judge_filenames(dirpath, filenames)
        self.logger.export(self, path, IS_LOG_IGNORED)

    def judge_dirnames(self, dirpath, dirnames):
        acted_dirs = []
        for dirname in dirnames:
            if not self.is_ignored_dir(dirname):
                if self.action_dir(dirpath, dirname):
                    acted_dirs.append(dirname)
            else:
                self.logger.add_ignored(dirpath, dirname)
        """ Remove dir that should be ignored from list. """
        dirnames[:] = acted_dirs

    def judge_filenames(self, dirpath, filenames):
        for filename in filenames:
            if not self.is_ignored_file(filename):
                self.action_file(dirpath, Filename(filename))
            else:
                self.logger.add_ignored(dirpath, filename)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def action_dir(self, dirpath, dirname):
        """ @Templete Method. Return True if this dir should be walked. """
        return True

    # noinspection PyMethodMayBeStatic
    def action_file(self, dirpath, filename):
        """ @Templete Method. """
        pass

    def is_ignored_dir(self, dirname):
        """ Check whether dirname start with ignored dir-prefix. """
        return any(prefix for prefix in self.ignored_dir_prefix if dirname.startswith(prefix))

    def is_ignored_file(self, filename):
        """ Check whether filename has extension in ignored extension. """
        return Filename(filename).extension in self.ignored_extension
