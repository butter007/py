# -*- coding: utf-8 -*- 
import xlrd
import datetime


path = "Z:/周德进口资金池.xls"
data = xlrd.open_workbook(path)


li = []
for i in range(len(data.sheet_names())):
    table = data.sheets()[i]
    nrows = table.nrows
    ncols = table.ncols
    sunrize = 0
    line = ""
    for j in range(1,nrows):
        if(table.cell(j,1).ctype!=0 and table.cell(j,1).ctype!=1):
            sunrize += float(table.cell(j,1).value)
    
    
    line = "%s：%.2f" % (data.sheet_names()[i],sunrize)
    li.append(line)


#写入txt
target = open("Z:/log.txt",'a+');
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
target.write(now_time)
target.write('\n')
for i in range(len(li)):
    target.write(li[i])
    target.write("\n")
target.write("--------------***************-----------------\n")
target.close()
