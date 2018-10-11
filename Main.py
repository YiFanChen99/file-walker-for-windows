# -*- coding:utf-8 -*-
"""
這個程式將走訪執行目錄下的所有資料夾，並執行某項操作
"""
from ModelUtility.Settings import OPERATION, TARGET
from Model.OperatorFactory import create_operator


if __name__ == '__main__':
    print("Target path is: \"{0}\".".format(TARGET))
    operator = create_operator(OPERATION)
    print("\tWith operator: \"{0}\"".format(operator.get_description()))
    print("\tWith config: \"{0}\"\n".format(operator.get_config()))
    message_execution = "Sure to execute? (1:Y 0:N)"
    isExecute = int(input(message_execution))
    if isExecute:
        for each_target in TARGET:
            operator.walk_and_action(each_target)
        print("Action done.")
    else:
        print("Action skipped.")
