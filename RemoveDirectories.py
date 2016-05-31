# -*- coding:utf-8 -*-
""" 這個程式能夠刪除所有在同目錄下的指定資料夾名稱（含子資料夾） """

import os
import shutil

FOLDER_NAME = 'PaxHeaders.20420'

def convert_all_files(path):
    for dirPath, dirNames, fileNames in os.walk(path):
        for dirName in dirNames:
            if dirName == FOLDER_NAME:
                shutil.rmtree(os.path.join(dirPath, dirName))
                print dirPath, '/', dirName, 'has been removed'

pathMessage = "目前路徑是：「" + os.getcwd() + "」\r\n"
print pathMessage
convert_all_files(os.getcwd())