import pandas as pd


def find_differences(first_file_name, second_file_name, connector=' AND', encode='utf-8', in_separator=',',
                     out_separator=',', first_col_list=False, second_col_list=False, drop_duplicates=True,
                     header_line=0, rows_to_skip=0, result_folder='', first_result_folder='', second_result_folder='',
                     missing_file_out='', sort_results=False):
    first_file_out = first_file_name.split('\\')[-1]
    second_file_out = second_file_name.split('\\')[-1]
    first_file_format = first_file_out.split('.')[-1]
    second_file_format = second_file_out.split('.')[-1]

    if result_folder and first_result_folder == '':
        first_result_folder = result_folder
    if result_folder and second_result_folder == '':
        second_result_folder = result_folder

    if first_file_format == 'xlsx' or first_file_format == 'xls':
        first_file = pd.read_excel(first_file_name, skiprows=rows_to_skip, header=header_line,
                                   encoding=encode, dtype='str')
    if first_file_format == 'xlsx' or first_file_format == 'xls':
        second_file = pd.read_excel(second_file_name, skiprows=rows_to_skip, header=header_line,
                                    encoding=encode, dtype='str')
    if first_file_format == 'csv':
        first_file = pd.read_csv(first_file_name, skiprows=rows_to_skip, header=header_line, encoding=encode,
                                 sep=in_separator, dtype='str')
    if second_file_format == 'csv':
        second_file = pd.read_csv(second_file_name, skiprows=rows_to_skip, header=header_line, encoding=encode,
                                  sep=in_separator, dtype='str')
    if first_col_list:
        first_file = first_file.iloc[:, first_col_list]
    if second_col_list:
        second_file = second_file.iloc[:, second_col_list]
    second_file.columns = first_file.columns

    if drop_duplicates:
        first_file.drop_duplicates(inplace=True)
        second_file.drop_duplicates(inplace=True)

    first_in_second = pd.merge(first_file, second_file, on=list(first_file.columns), how='left', indicator='Exist')
    second_in_first = pd.merge(second_file, first_file, on=list(first_file.columns), how='left', indicator='Exist')

    first_in_second_diff = first_in_second.loc[first_in_second['Exist'] != 'both', first_file.columns]
    second_in_first_diff = second_in_first.loc[second_in_first['Exist'] != 'both', first_file.columns]

    if sort_results:
        first_in_second_diff_sorted = first_in_second_diff.sort_values(by=first_file.columns[0])
        second_in_first_diff_sorted = second_in_first_diff.sort_values(by=first_file.columns[0])
    else:
        first_in_second_diff_sorted = first_in_second_diff
        second_in_first_diff_sorted = second_in_first_diff

    with open(result_folder + r'missing_lines_' + missing_file_out + '.txt', 'w', encoding=encode) as outfile:
        outfile.write('Lines missing in ' + first_file_name + ': %s\n' % second_in_first_diff_sorted.shape[0])
        for row in second_in_first_diff_sorted.iterrows():
            str_list = [str(column) + ' = \'' + str(value) + '\'' for column, value in
                        zip(first_file.columns, row[1].values)]
            str_joined = connector.join(str_list) + '\n'
            outfile.write(str_joined)

        outfile.write('\n\nLines missing in ' + second_file_name + ': %s\n' % first_in_second_diff_sorted.shape[0])
        for row in first_in_second_diff_sorted.iterrows():
            str_list = [str(column) + ' = \'' + str(value) + '\'' for column, value in
                        zip(first_file.columns, row[1].values)]
            str_joined = connector.join(str_list) + '\n'
            outfile.write(str_joined)

    first_clean_name = first_file_out.split('.')[-2]
    second_clean_name = second_file_out.split('.')[-2]
    if out_separator:
        first_in_second_diff_sorted.to_csv(second_result_folder + r'missing_lines_' + second_clean_name + '.csv',
                                           sep=out_separator, encoding=encode, index=False)
        second_in_first_diff_sorted.to_csv(first_result_folder + r'missing_lines_' + first_clean_name + '.csv',
                                           sep=out_separator, encoding=encode, index=False)
