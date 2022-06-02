# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import xlrd as xlrd
import xlwt



# Press the green button in the gutter to run the script.
def readText():
    workbook = xlrd.open_workbook_xls("豆瓣电影Top250.xls")
    table = workbook.sheets()[0]
    table0 = workbook.sheet_by_index(0)
    #按行读取
    # for i in range(table.nrows):
    #     print(table.row_values(i))
    #按列读取
    # for i in range(table.ncols):
    #     print(table.col_values(i))
    print(table.cell(3, 2).value)
    pass


if __name__ == '__main__':
    readText()



