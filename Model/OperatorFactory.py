# -*- coding: utf-8 -*-
from Model.Actor.DirectoryRemover import DirectoryRemover
from Model.Actor.TxtFileCreator import TxtFileCreator

OPERATORS = [TxtFileCreator, DirectoryRemover]


def create_operator(operator_id):
    operator_map = {each_operator.get_id(): each_operator for each_operator in OPERATORS}
    if operator_id in operator_map:
        return operator_map[operator_id]()
    else:
        raise Exception("Operation id not found.")
