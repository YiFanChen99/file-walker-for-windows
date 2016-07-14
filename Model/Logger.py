# -*- coding: utf-8 -*-
import json
from datetime import datetime


class Logger(object):
    def __init__(self, log_path):
        self.log_path = log_path
        self.acted_file = []
        self.ignored_dir = []
        self.ignored_file = []

    def add_acted_file(self, dirpath, filename):
        self.acted_file.append(dirpath + filename)

    def add_ignored_dir(self, dirpath):
        self.ignored_dir.append(dirpath)

    def add_ignored_file(self, dirpath, filename):
        self.ignored_file.append(dirpath + filename)

    def export(self, the_operator, is_ignored_dir_included=False, is_ignored_file_included=False):
        with open(self.log_path, 'a') as log_file:
            description = '\n\n{0}\n{1}: {2}\n'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M'), the_operator.__name__, the_operator.get_description())
            log_file.write(description)

            result = [
                {'Acted files': self.acted_file}
            ]
            if is_ignored_dir_included:
                result.append({'Ignored dirs:': self.ignored_dir})
            if is_ignored_file_included:
                result.append({'Ignored files:': self.ignored_file})
            json.dump(result, log_file, indent=4, separators=(',', ': '))
        self.clear()

    def clear(self):
        self.acted_file = []
        self.ignored_dir = []
        self.ignored_file = []
