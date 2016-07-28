# -*- coding: utf-8 -*-
import os.path
import shutil

from Model.Actor.Walker import Walker
from ModelUtility.CommonValue import DIRECTORY_REMOVER_ID
from ModelUtility.Settings import TARGET_NAME


class DirectoryRemover(Walker):
    @staticmethod
    def get_id():
        return DIRECTORY_REMOVER_ID

    @staticmethod
    def get_description():
        return "Removing each directory with specific name. Including every dirs/files below."

    @staticmethod
    def get_config():
        return {'Dir name': TARGET_NAME}

    def action_dir(self, dir_path, dir_name):
        if dir_name in TARGET_NAME:
            shutil.rmtree(os.path.join(dir_path, dir_name))
            self.logger.add_acted(dir_path, dir_name)
            return False
        return True
