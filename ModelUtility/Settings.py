# -*- coding: utf-8 -*-

OPERATION = 'dirr'

IGNORED_DIR_PREFIX = ['.', '_']  # 預設不處理的目錄之前綴
IGNORED_EXTENSION = ['.py', '.pyc', '', '.md']  # 預設不處理的檔案類型
NEW_FILE_AT_TOP = False  # 建立的檔案一律放於執行目錄下，不對應其原檔案位置擺放
TARGET_NAME = ['MyName']  # 限定處理特定的目錄或檔案

FILE_PROCESS_LOG = 'log.txt'
IS_LOG_IGNORED = False
