# -*- coding:utf-8 -*-
"""
這個程式將走訪執行目錄下的所有資料夾，並執行某項操作
"""
import os
from ModelUtility.Settings import OPERATION
from ModelUtility.CommonValue import CURRENT_PATH
from Model.Walker import Walker
from Model.OperatorFactory import create_operator


if __name__ == '__main__':
    print("Current path is: \"{0}\".".format(os.getcwd()))
    operator = create_operator(OPERATION)
    print("With operator: \"{0}\"\r\n".format(operator.get_description()))
    message_execution = "Sure to execute? (1:Y 0:N)"
    isExecute = int(input(message_execution))
    if isExecute:
        walker = Walker()
        walker.walk_and_call_action(operator, CURRENT_PATH)
        print("Action done.")
    else:
        print("Action skipped.")
