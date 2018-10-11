# -*- coding: utf-8 -*-
from Model.Actor.Walker import Walker
from ModelUtility.CommonValue import OP


class DoNothing(Walker):
    @staticmethod
    def get_id():
        return OP.DO_NOTHING

    @staticmethod
    def get_description():
        return "Go through each dir/file and do nothing."

    @staticmethod
    def get_config():
        return {}

    def action_dir(self, dirpath, dirname):
        self.logger.add_acted(dirpath, dirname)
        return True

    # noinspection PyMethodMayBeStatic
    def action_file(self, dirpath, filename):
        self.logger.add_acted(dirpath, filename.name)
        pass
