# compare_files

This script can be used to compare multiple pairs of .csv or .xlsx files. 

## Parameters
__FIRST_FOLDER__ – specifies path to the folder with first set of files\
__SECOND_FOLDER__ – specifies path to the folder with second set of files. Corresponding files in FIRST_FOLDER and SECOND_FOLDER may have different names. Which file corrensponds to a given file is determined by order of files in their folders\
__FIRST_FILES_LIST__ – list of strings, determines which files from FIRST_FOLDER will be used, it may be used to determine order of files, when [] then all files from FIRST_FOLDER will be used\
__SECOND_FILES_LIST__ – list of strings, determines which files from SECOND_FOLDER will be used, it may be used to determine order of files, when [] then all files from SECOND_FOLDER will be used\
__RESULT_FOLDER__ – path to folder in which missing_lines_[first_filename]_[second_file_name] files will be saved\
__FIRST_RESULT_FOLDER__ – path to folder in which missing_lines_[first_filename] files will be saved\
__SECOND_RESULT_FOLDER__ – path to folder in which missing_lines_[second_filename] files will be saved\
__CONNECTOR__ – string, determines connector between columns in missing_lines_[first_filename]_[second_file_name] files\
__ENCODING__ – string, encoding of .csv files\
__IN_SEPARATOR__ – string, separator of .csv files in FIRST_FOLDER and SECOND_FOLDER\
__OUT_SEPARATOR__ – string, separator of .csv files in FIRST_RESULT_FOLDER and SECOND_RESULT_FOLDER\
__COL_LIST__ – list of integers, list of column numbers which will be used, if False then all columns will be used\
__DROP_DUPLICATES__ – True\False, if False duplicated rows in output files may appear\
__HEADER_LINE__ – None or integer, number of row in which there are column names\
__ROWS_TO_SKIP__ – integer, number of rows to skip
