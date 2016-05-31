# -*- coding:utf-8 -*-

'''
這個程式能夠為同目錄下的所有檔案（含子資料夾）都建立一個同名的txt檔
'''

import os

def create_txt_file(fileSimpleName):
    fileName = (fileSimpleName + ".txt")
    fileopen = open(fileName,'w')
    #fileopen.write(p)
    fileopen.close()

def convert_all_files(path):
    for dirPath, dirNames, fileNames in os.walk(path):
        for fileName in fileNames:
            partialNames = os.path.splitext(fileName)
            # 純文字檔不必轉，python檔也預設不轉
            if partialNames[1] != ".txt" and partialNames[1] != ".py":
                create_txt_file(partialNames[0])

pathMessage = "目前路徑是：「" + os.getcwd() + "」\r\n" + "確定要執行嗎？(1:Y 0:N)"
isExecute = int(input(pathMessage))
if(isExecute):
    program = convert_all_files("./")
