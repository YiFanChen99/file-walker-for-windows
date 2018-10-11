# -*- coding: utf-8 -*-
from ModelUtility.CommonValue import OP, WALKING_DIR_PATH

OPERATION = OP.DO_NOTHING
TARGET = WALKING_DIR_PATH or ["D:\\Temp\\megaPics"]

IGNORED_DIR_PREFIX = ['.', '_']  # 預設不處理的目錄之前綴
IGNORED_EXTENSION = ['.py', '.pyc', '', '.md']  # 預設不處理的檔案類型
FILE_PROCESS_LOG = 'log.txt'  # log 輸出檔名
IS_LOG_IGNORED = False  # 是否特別記錄略過不處理的檔案於 log 中

''' Used in specific actors. '''
NEW_FILE_AT_TOP = False  # 建立的檔案一律放於執行目錄下，不對應其原檔案位置擺放  User: TxtFileCreator
TARGET_NAME = ['MyName']  # 限定處理特定的目錄或檔案  User: DirectoryRemover, ManyFileCreator
REPETITION = 900  # 反覆次數  User: ManyFileCreator
