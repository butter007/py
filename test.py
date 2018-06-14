# -*- coding: utf-8 -*-
from pyExcelerator import *
import datetime
import sys
import xlrd
import pickle

with open('data.pkl') as f:
    adic = pickle.load(f)
print adic['SUZJ1710056K']

alldata6002 = xlrd.open_workbook("D:\py\\new6002all.xls")
alltable6002 = alldata6002.sheets()[0]

alldata6601 = xlrd.open_workbook("D:\py\\new6601all.xls")
alltable6601 = alldata6601.sheets()[0]

alldata6603 = xlrd.open_workbook("D:\py\\new6603all.xls")
alltable6603 = alldata6603.sheets()[0]

# {6002: [39900, 39946], 6603: [3633]}
tenlist = []

for data in adic.keys():
    if not isinstance(data, basestring):
        continue
    if data.startswith('SUZJ1607') or data.startswith('SUZJ1707'):
        drtotal = 0
        crtotal = 0
        name = ''
        foreignmoney = 0
        if adic[data].get(6002):
            list6002 = adic[data].get(6002)
            for lidata in list6002:
                row6002 = alltable6002.row_values(lidata)
                del (row6002[3])
                del (row6002[6:11])
                del (row6002[7:9])
                if row6002[9]:
                    drtotal += row6002[9]
                if row6002[10]:
                    crtotal += row6002[10]
                tenlist.append(row6002)
                if not name:
                    name = row6002[6]
                if (not foreignmoney) and row6002[3] == u'销售':
                    foreignmoney = row6002[8]
        if adic[data].get(6601):
            list6601 = adic[data].get(6601)
            for lidata in list6601:
                row6601 = alltable6601.row_values(lidata)
                del (row6601[3])
                del (row6601[5])
                del (row6601[6])
                row6601.insert(7, '')
                row6601.insert(8, '')
                if row6601[9]:
                    drtotal += row6601[9]
                if row6601[10]:
                    crtotal += row6601[10]
                if not name:
                    name = row6601[6]
                tenlist.append(row6601)
        if adic[data].get(6603):
            list6603 = adic[data].get(6603)
            for lidata in list6603:
                row6603 = alltable6603.row_values(lidata)
                del (row6603[3])
                del (row6603[6])
                row6603.insert(7, '')
                row6603.insert(8, '')
                if row6603[9]:
                    drtotal += row6603[9]
                if row6603[10]:
                    crtotal += row6603[10]
                if not name:
                    name = row6603[6]
                tenlist.append(row6603)

        percent = 0
        lirun = crtotal - drtotal
        if foreignmoney:
            percent = round(lirun / foreignmoney, 2)
        tenlist.append(['', '', '', '', '', '', name, '', foreignmoney, drtotal, crtotal, lirun, percent])

excle_Workbook = Workbook()
excel_sheet_name = datetime.datetime.now().strftime('%Y-%m-%d')
excel_sheet = excle_Workbook.add_sheet(excel_sheet_name)

index = 0
print len(tenlist)
if tenlist:
    for data in tenlist:
        for i in range(len(data)):
            excel_sheet.write(index, i, data[i])
        index += 1

excle_Workbook.save('D:\py\\tenlirun.xls')
