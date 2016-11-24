# -*- coding: utf-8 -*-
import os.path

from Model.Actor.Walker import Walker
from ModelUtility.CommonValue import MANY_FILE_CREATOR_ID
from ModelUtility.Settings import TARGET_NAME, REPETITION


class ManyFileCreator(Walker):
    @staticmethod
    def get_id():
        return MANY_FILE_CREATOR_ID

    @staticmethod
    def get_description():
        return "Creating many txt files with trivial ID and content."

    @staticmethod
    def get_config():
        return {}

    def action_dir(self, dir_path, dir_name):
        if dir_name in TARGET_NAME:
            prefix_path = os.path.join(dir_path, dir_name) + '/'
            for i in range(REPETITION):
                ManyFileCreator.create_file(prefix_path, str(i))
            self.logger.add_acted(dir_path, dir_name)
            return False
        return True

    @staticmethod
    def create_file(dir_path, file_id):
        file_path = "{0}{1}.txt".format(dir_path, file_id)
        with open(file_path, 'w') as the_file:
            the_file.write(file_id + '\n')
