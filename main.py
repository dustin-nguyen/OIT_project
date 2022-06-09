# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Need xlrd  to read an excel file using Python
import xlrd
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find(dbPath, val, sheetName=None):
    df = pd.read_excel(dbPath, sheet_name=sheetName)
    print(df.loc[df['Name'] == val])
    # print(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Give the location of the file
    loc = ("db/datasheet.xlsx ")
    find(loc, "17F", "Sheet1")
    find(loc, "17F", "Sheet2")
    find(loc, "18H", "Sheet1")
    find(loc, "18H", "Sheet2")
    # print("data from sheet 1")
    # df1 = pd.read_excel(loc, sheet_name="Sheet1")
    # print(df1)
    #
    # print("data from sheet 2")
    # df2 = pd.read_excel(loc, sheet_name="Sheet2")
    # print(df2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
