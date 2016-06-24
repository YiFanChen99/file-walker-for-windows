# -*- coding: utf-8 -*-
from ModelUtility.CommonValue import CURRENT_PATH, TXT_FILE_CREATOR_ID
from ModelUtility.Settings import NEW_FILE_AT_TOP


class TxtFileCreator(object):
    @staticmethod
    def get_id():
        return TXT_FILE_CREATOR_ID

    @staticmethod
    def get_description():
        return "Creating empty txt file for each file."

    @staticmethod
    def action(dir_path, filename):
        TxtFileCreator.create_txt_file(dir_path, filename.simple_name)

    @staticmethod
    def create_txt_file(dir_path, simple_filename):
        file_path = TxtFileCreator.compose_file_path(dir_path, simple_filename)
        file = open(file_path, 'w')
        file.close()

    @staticmethod
    def compose_file_path(dir_path, simple_filename):
        corresponding_dirpath = CURRENT_PATH if NEW_FILE_AT_TOP else \
            (dir_path if dir_path == CURRENT_PATH else dir_path + '/')
        return "{0}{1}.txt".format(corresponding_dirpath, simple_filename)
