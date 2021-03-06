# -*- coding: utf-8 -*-
from Model.Actor.Walker import Walker
from ModelUtility.CommonValue import EXE_PATH, OP
from ModelUtility.Settings import NEW_FILE_AT_TOP


class TxtFileCreator(Walker):
    @staticmethod
    def get_id():
        return OP.TXT_FILE_CREATOR

    @staticmethod
    def get_description():
        return "Creating empty txt file for each file."

    @staticmethod
    def get_config():
        return {}

    def __init__(self, **kwargs):
        Walker.__init__(self, **kwargs)
        # Avoiding cleanup txt file
        self.ignored_extension.append('.txt')

    def action_file(self, dir_path, filename):
        TxtFileCreator.create_txt_file(dir_path, filename.simple_name)
        self.logger.add_acted(dir_path, filename.name)

    @staticmethod
    def create_txt_file(dir_path, simple_filename):
        file_path = TxtFileCreator.compose_file_path(dir_path, simple_filename)
        file = open(file_path, 'w')
        file.close()

    @staticmethod
    def compose_file_path(dir_path, simple_filename):
        corresponding_dir_path = EXE_PATH if NEW_FILE_AT_TOP else \
            (dir_path if dir_path == EXE_PATH else dir_path + '/')
        return "{0}{1}.txt".format(corresponding_dir_path, simple_filename)
