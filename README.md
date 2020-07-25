# compare_files

This script can be used to compare multiple pairs of .csv or .xlsx files. 

## Parameters
FIRST_FOLDER – specifies path to the folder with first set of files
SECOND_FOLDER– specifies path to the folder with second set of files
Corresponding files in FIRST_FOLDER and SECOND_FOLDER may have different names. Which file corrensponds to a given file is determined by order of files in their folders.
FIRST_FILES_LIST – list of strings, determines which files from FIRST_FOLDER will be used, it may be used to determine order of files, when [] then all files from FIRST_FOLDER will be used
SECOND_FILES_LIST – list of strings, determines which files from SECOND_FOLDER will be used, it may be used to determine order of files, when [] then all files from SECOND_FOLDER will be used
RESULT_FOLDER – path to folder in which missing_lines_[first_filename]_[second_file_name] files will be saved
FIRST_RESULT_FOLDER – path to folder in which missing_lines_[first_filename] files will be saved
SECOND_RESULT_FOLDER – path to folder in which missing_lines_[second_filename] files will be saved
CONNECTOR – string, determines connector between columns in missing_lines_[first_filename]_[second_file_name] files
ENCODING – string, encoding of .csv files
IN_SEPARATOR – string, separator of .csv files in FIRST_FOLDER and SECOND_FOLDER
OUT_SEPARATOR – string, separator of .csv files in FIRST_RESULT_FOLDER and SECOND_RESULT_FOLDER
COL_LIST – list of integers, list of column numbers which will be used, if False then all columns will be used
 DROP_DUPLICATES – True\False, if False duplicated rows in output files may appear
HEADER_LINE – None or integer, number of row in which there are column names
ROWS_TO_SKIP – integer, number of rows to skip







