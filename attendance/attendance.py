import xlrd

from Common.common import table_data_list
from Common.convert2md import convert2md
from Common.convert2md import initmd


def handle(file):
    # 初始化md文件
    initmd()
    print(file)
    # file = '/Users/yanbo/Desktop/外出考勤日报表1026.xlsx'
    data = xlrd.open_workbook(file)
    table = data.sheets()

    merge_data = []

    # table_length = len(table) # 表的长度
    first_table = data.sheet_by_index(0)
    second_table = data.sheet_by_index(1)

    second_table_data_list = table_data_list(second_table)

    output = []

    first_table_nrow = first_table.nrows
    for i in range(3, first_table_nrow):
        row_value = first_table.row_values(i)
        row_value.pop()
        out = u" | ".join(row_value)
        for j in range(0, len(second_table_data_list)):
            if(second_table_data_list[j][0] == row_value[0] and second_table_data_list[j][2] == row_value[2] and second_table_data_list[j][5] == row_value[5]):
                out += " | {} ".format(second_table_data_list[j][6])
            if(second_table_data_list[j][0] == row_value[0] and second_table_data_list[j][2] == row_value[2] and second_table_data_list[j][5] == row_value[4]):
                out += " | {}".format(second_table_data_list[j][6])
                second_table_data_list.remove(second_table_data_list[j])
                merge_data.append(out)
                out = ''
                break
        # convert2md(out)

    return merge_data
