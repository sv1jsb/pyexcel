"""
read_cell_by_cell.py
:copyright: (c) 2014 by C. W.
:license: GPL v3

This shows how to use **Reader** class to go through a single
page spreadsheet, The output is::

    1.0
    2.0
    3.0
    4.0
    5.0
    6.0
    7.0
    8.0
    9.0

"""

import pyexcel

# Simple give the file name to **Reader**
# "example.xls","example.xlsx","example.ods", "example.xlsm"
spreadsheet = pyexcel.Reader("example.csv") 

# row_range() gives [0 .. number of rows]
for r in spreadsheet.row_range():
    # column_range() gives [0 .. number of ranges]
    for c in spreadsheet.column_range():
        # cell_value(row_index, column_index)
        # return the value at the specified
        # position
        # please note that both row_index
        # and column_index starts from 0
        print(spreadsheet.cell_value(r, c))