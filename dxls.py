# -*- coding: utf-8 -*- 
import xlrd
import datetime
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

#xlrd.Book.encoding = "utf-8"

path = "Z:\周德进口资金池.xls"
path = path.decode('utf-8')
data = xlrd.open_workbook(path)


li = []
for i in range(len(data.sheet_names())):
    table = data.sheets()[i]
    nrows = table.nrows
    ncols = table.ncols
    sunrize = 0
    #print float(table.cell(1,1).value)
    line = ""
    for j in range(1,nrows):
        if(table.cell(j,1).ctype!=0 and table.cell(j,1).ctype!=1):
            sunrize += float(table.cell(j,1).value)
    
    
#    sunrize = format(sunrize,',')
    line = "%s：%.2f" % (data.sheet_names()[i].decode('utf-8'),sunrize)
    li.append(line)


target = open("Z:\log.txt",'a+');
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
target.write(now_time)
target.write('\n')
for i in range(len(li)):
    target.write(li[i])
    target.write("\n")
target.write("--------------***************-----------------\n")
target.close()
