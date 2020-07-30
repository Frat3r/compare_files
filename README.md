# compare_files

This script can be used to compare multiple pairs of .csv or .xlsx files. 
## Requirements
The basic requirements are 
* [python 3](https://www.python.org/downloads/release/python-385/) 
* pandas (to install it in cmd use _cd_ _\[Path_to_Python_folder\]\Python38\Scripts_, then _pip.exe install pandas_)
 
I recommend using [Anaconda](https://www.anaconda.com/products/individual) - it contains everything what is needed.

## Executing
To use script edit _compare_files.py_ file with any text editor and change the parameters according to your needs (especially __FIRST_FOLDER__ and __SECOND_FOLDER__). After that run _compare_files.py_ from console by  
_\[Path_to_Python_folder\]\Python38\python.exe_ _\[Path_to_compare_files\]\compare_files.py_  
(or you may just use IDE like PyCharm or Spyder).   
Result of executing file _compare_files.py_ for pairs (A_1,B_1), ..., (A_n,B_n) are three sets of files:
* missing_lines_A_1\_B_1.txt, missing_lines_A_2\_B_2.txt, ..., missing_lines_A_n\_B_n.txt
* missing_lines_A_1.csv, missing_lines_A_2.csv,..., missing_lines_A_n.csv
* missing_lines_B_1.csv, missing_lines_B_2.csv,..., missing_lines_B_n.csv

## Parameters
__FIRST_FOLDER__ – specifies path to the folder with first set of files\
__SECOND_FOLDER__ – specifies path to the folder with second set of files. Corresponding files in FIRST_FOLDER and SECOND_FOLDER may have different names. Which file corrensponds to a given file is determined by order of files in their folders\
__FIRST_FILES_LIST__ – list of strings, determines which files from FIRST_FOLDER will be used, it may be used to determine order of files, if [] then all files from FIRST_FOLDER will be used\
__SECOND_FILES_LIST__ – list of strings, determines which files from SECOND_FOLDER will be used, it may be used to determine order of files, if [] then all files from SECOND_FOLDER will be used\
__RESULT_FOLDER__ – path to folder in which missing_lines_[first_filename]\_[second_file_name].txt files will be saved, if specified folder doesn't exist then it will be created automatically\
__FIRST_RESULT_FOLDER__ – path to folder in which missing_lines_[first_filename].csv files will be saved, if specified folder doesn't exist then it will be created automatically\
__SECOND_RESULT_FOLDER__ – path to folder in which missing_lines_[second_filename].csv files will be saved, if specified folder doesn't exist then it will be created automatically\
__CONNECTOR__ – string, determines connector between columns in missing_lines_[first_filename]\_[second_file_name].txt files\
__ENCODING__ – string, encoding of .csv files\
__IN_SEPARATOR__ – string, separator of .csv files in FIRST_FOLDER and SECOND_FOLDER\
__OUT_SEPARATOR__ – string, separator of .csv files in FIRST_RESULT_FOLDER and SECOND_RESULT_FOLDER\
__COL_LIST__ – list of integers, list of column numbers which will be used, if False then all columns will be used\
__DROP_DUPLICATES__ – True\False, if False duplicated rows in output files may appear\
__HEADER_LINE__ – None or integer, row number with column names\
__ROWS_TO_SKIP__ – integer, number of rows to skip
