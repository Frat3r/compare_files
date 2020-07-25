import os
from find_differences import *
from pathlib import Path

FIRST_FOLDER = r'Example\Test_files\Test1\\'
SECOND_FOLDER = r'Example\Test_files\Test2\\'
FIRST_FILES_LIST = []
SECOND_FILES_LIST = []
RESULT_FOLDER = r'Example\Results\\'
FIRST_RESULT_FOLDER = r'Example\Results\Test1\\'
SECOND_RESULT_FOLDER = r'Example\Results\Test2\\'
#  FIRST_FILE_NAME = 'from_base.csv'
#  SECOND_FILE_NAME = 'from_export.csv'
#  FILES_FORMAT = '.csv'
CONNECTOR = ' AND '
ENCODING = 'utf-8'
IN_SEPARATOR = ','
OUT_SEPARATOR = ','
FIRST_COL_LIST = False  # [0, 2]
SECOND_COL_LIST = False  # [0, 2]
DROP_DUPLICATES = True
HEADER_LINE = 0  # 0, int, None
ROWS_TO_SKIP = 0

if RESULT_FOLDER:
    Path(RESULT_FOLDER).mkdir(parents=True, exist_ok=True)
if FIRST_RESULT_FOLDER:
    Path(FIRST_RESULT_FOLDER).mkdir(parents=True, exist_ok=True)
if SECOND_RESULT_FOLDER:
    Path(SECOND_RESULT_FOLDER).mkdir(parents=True, exist_ok=True)

first_files_list = FIRST_FILES_LIST
second_files_list = SECOND_FILES_LIST
if FIRST_FOLDER and len(FIRST_FILES_LIST) == 0:
    first_files_list = os.listdir(FIRST_FOLDER)
if SECOND_FOLDER and len(SECOND_FILES_LIST) == 0:
    second_files_list = os.listdir(SECOND_FOLDER)
first_files_list = [FIRST_FOLDER + filename for filename in first_files_list]
second_files_list = [SECOND_FOLDER + filename for filename in second_files_list]
for first, second in zip(first_files_list, second_files_list):
    missing_out_name = first.split('\\')[-1].split('.')[-2] + '_' + second.split('\\')[-1].split('.')[-2]
    find_differences(first_file_name=first, second_file_name=second, connector=CONNECTOR, encode=ENCODING,
                     in_separator=IN_SEPARATOR, out_separator=OUT_SEPARATOR, first_col_list=FIRST_COL_LIST,
                     second_col_list=SECOND_COL_LIST, drop_duplicates=DROP_DUPLICATES, header_line=HEADER_LINE,
                     rows_to_skip=ROWS_TO_SKIP, result_folder=RESULT_FOLDER, first_result_folder=FIRST_RESULT_FOLDER,
                     second_result_folder=SECOND_RESULT_FOLDER, missing_file_out=missing_out_name)
