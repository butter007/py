# -*- coding: utf-8 -*-

import xlrd
from operator import itemgetter
from itertools import groupby

excel = xlrd.open_workbook("D:\py\\22220101zm.xlsx")
excel_table = excel.sheets()[0]
excel_title = excel_table.row_values(0)
li = []
for i in range(1, excel_table.nrows):
    dict1 = dict(zip(excel_title, excel_table.row_values(i)))
    li.append(dict1)
print len(li)
li.sort(key=itemgetter(excel_title[6]))
lig = groupby(li, itemgetter(excel_title[6]))
print excel_title[13]
for key, group in lig:
    i = 0
    j = 0
    for g in group:
        if g[excel_title[13]]:
            i += g[excel_title[13]]
        if g[excel_title[14]]:
            j += g[excel_title[14]]
        #    print key, i,j
    k = i - j
#    print i,j,k
    if abs(k) > 10:
        print key, abs(k)
