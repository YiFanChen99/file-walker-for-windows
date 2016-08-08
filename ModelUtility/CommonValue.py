# -*- coding: utf-8 -*-
import os
import sys

EXE_PATH = os.path.dirname(sys.argv[0])
LOG_FILE_PATH = str.format('{0}{1}{2}', EXE_PATH, os.path.sep, 'log.txt')
WALKING_DIR_PATH = sys.argv[1:]

# Operation id
TXT_FILE_CREATOR_ID = 'txtc'
DIRECTORY_REMOVER_ID = 'dirr'
DO_NOTHING_ID = 'don'
