# -*- coding: utf-8 -*-
from pyExcelerator import *
import datetime
import sys
import xlrd
import pickle
from xlutils.copy import copy

reload(sys)
sys.setdefaultencoding('utf-8')

eledata600211 = xlrd.open_workbook("D:\py\\600211.xlsx")
eletable600211 = eledata600211.sheets()[0]
nrows600211 = eletable600211.nrows

eledata660111 = xlrd.open_workbook("D:\py\\660111.xlsx")
eletable660111 = eledata660111.sheets()[0]
nrows660111 = eletable660111.nrows

eledata660311 = xlrd.open_workbook("D:\py\\660311.xlsx")
eletable660311 = eledata660311.sheets()[0]
nrows660311 = eletable660311.nrows

data6002 = xlrd.open_workbook("D:\py\\6002all.xlsx")
table6002 = data6002.sheets()[0]
nrows6002 = table6002.nrows
excel6002 = copy(data6002)
sheet6002 = excel6002.get_sheet(0)
row6002 = nrows6002

for i in xrange(1, nrows600211):
    for j, data in enumerate(eletable600211.row_values(i)):
        sheet6002.write(row6002 + i - 1, j, data)
excel6002.save('new6002all.xls')

data6601 = xlrd.open_workbook("D:\py\\6601all.xlsx")
table6601 = data6601.sheets()[0]
nrows6601 = table6601.nrows
excel6601 = copy(data6601)
sheet6601 = excel6601.get_sheet(0)
row6601 = nrows6601

for i in xrange(1, nrows660111):
    for j, data in enumerate(eletable660111.row_values(i)):
        sheet6601.write(row6601 + i - 1, j, data)
excel6601.save('new6601all.xls')


data6603 = xlrd.open_workbook("D:\py\\6603all.xlsx")
table6603 = data6603.sheets()[0]
nrows6603 = table6603.nrows
excel6603 = copy(data6603)
sheet6603 = excel6603.get_sheet(0)
row6603 = nrows6603

for i in xrange(1, nrows660311):
    for j, data in enumerate(eletable660311.row_values(i)):
        sheet6603.write(row6603 + i - 1, j, data)
excel6603.save('new6603all.xls')

'''
alldata6601 = xlrd.open_workbook("D:\py\\6601all.xlsx")
alltable6601 = alldata6601.sheets()[0]
allnrows6601 = alltable6601.nrows
col6601 = alltable6601.col_values(7)
new_col6601 = set(col6601)

alldata6603 = xlrd.open_workbook("D:\py\\6603all.xls")
alltable6603 = alldata6603.sheets()[0]
allnrows6603 = alltable6603.nrows
col6603 = alltable6603.col_values(6)
new_col6603 = set(col6603)
'''
alldata6002 = xlrd.open_workbook("D:\py\\new6002all.xls")
alltable6002 = alldata6002.sheets()[0]
allnrows6002 = alltable6002.nrows
col6002 = alltable6002.col_values(6)
new_col6002 = set(col6002)

alldata6601 = xlrd.open_workbook("D:\py\\new6601all.xls")
alltable6601 = alldata6601.sheets()[0]
allnrows6601 = alltable6601.nrows
col6601 = alltable6601.col_values(7)
new_col6601 = set(col6601)

alldata6603 = xlrd.open_workbook("D:\py\\new6603all.xls")
alltable6603 = alldata6603.sheets()[0]
allnrows6603 = alltable6603.nrows
col6603 = alltable6603.col_values(6)
new_col6603 = set(col6603)

allyunbian = new_col6002 | new_col6601 | new_col6603
print len(allyunbian)

adic = {}
for data in allyunbian:
    for j in range(1, allnrows6002):
        row = alltable6002.row_values(j)
        if data == row[6]:
            adic.setdefault(data, {}).setdefault(6002, []).append(j)

for data in allyunbian:
    for j in range(1, allnrows6601):
        row = alltable6601.row_values(j)
        if data == row[7]:
            adic.setdefault(data, {}).setdefault(6601, []).append(j)

for data in allyunbian:
    for j in range(1, allnrows6603):
        row = alltable6603.row_values(j)
        if data == row[6]:
            adic.setdefault(data, {}).setdefault(6603, []).append(j)

output = open('data.pkl', 'wb')
pickle.dump(adic, output)
output.close()

'''
excle_Workbook = Workbook()
excel_sheet_name = datetime.datetime.now().strftime('%Y-%m-%d')
excel_sheet = excle_Workbook.add_sheet(excel_sheet_name)
'''
