# -*- coding: utf-8 -*-
import json
from datetime import datetime


class Logger(object):
    def __init__(self, log_path):
        self.log_path = log_path
        self.acted = []
        self.ignored = []

    def add_acted(self, dirpath, name):
        self.acted.append(dirpath + '/' + name)

    def add_ignored(self, dirpath, name):
        self.ignored.append(dirpath + '/' + name)

    def export(self, the_operator, path, is_ignored_included=False):
        with open(self.log_path, 'a') as log_file:
            description = '\n\n{0}\n{1}: {2}\n'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M'), type(the_operator).__name__, the_operator.get_description())
            description += '\twith path: {}\n'.format(path)
            description += '\twith config: {}\n'.format(the_operator.get_config())
            log_file.write(description)

            result = [
                {'Acted': self.acted}
            ]
            if is_ignored_included:
                result.append({'Ignored:': self.ignored})
            json.dump(result, log_file, indent=4, separators=(',', ': '))
        self.clear()

    def clear(self):
        self.acted = []
        self.ignored = []
