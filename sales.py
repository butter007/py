import xlrd
import MySQLdb as db
import  time
sales = xlrd.open_workbook("D:\py\\6002.xlsx")
salestable = sales.sheets()[0]
nrows = salestable.nrows
print nrows
try:
    conn = db.connect(host='localhost',user='root',passwd='123',db='test',charset='utf8')
    cursor = conn.cursor()
except BaseException as e:
    print e
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS SALES(
                                id INT NOT NULL AUTO_INCREMENT,
                                part VARCHAR(20) NOT NULL,
                                proofdate VARCHAR(20) NOT NULL,
                                proofnum INT NOT NULL ,
                                summary VARCHAR (100),
                                zimu VARCHAR (10),
                                ximu VARCHAR (10),
                                yunbiannum VARCHAR (20),
                                salescontact VARCHAR (20),
                                fob VARCHAR (10),
                                country VARCHAR (10),
                                goodsname VARCHAR (20),
                                partwo VARCHAR(20) NOT NULL,
                                salername VARCHAR (10),
                                packae INT,
                                quanlity FLOAT ,
                                money VARCHAR (10),
                                originmoney FLOAT ,
                                cr FLOAT ,
                                dr FLOAT ,
                                PRIMARY KEY(id)
                               )ENGINE=MyISAM DEFAULT CHARSET=utf8''')
    starttime = time.time()
    for i in range(2,nrows):
        row = salestable.row_values(i)
        if not row[13]:
            row[13] = 0
        if not row[14]:
            row[14] = 0
        if not row[16]:
            row[16] = 0
        if not row[17]:
            row[17] = 0
        if not row[18]:
            row[18] = 0
        tup = tuple(row)
        sql = '''insert into sales(
                                part,
                                proofdate ,
                                proofnum ,
                                summary ,
                                zimu ,
                                ximu ,
                                yunbiannum ,
                                salescontact ,
                                fob ,
                                country ,
                                goodsname ,
                                partwo ,
                                salername ,
                                packae ,
                                quanlity ,
                                money ,
                                originmoney ,
                                cr ,
                                dr 
                                    ) values("%s","%s","%d","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%d","%.2f","%s","%.2f","%.2f","%.2f")''' %tup
        cursor.execute(sql)
        conn.commit()
except BaseException as e:
    print e
finally:
    cursor.close()
    endtime = time.time()
    print endtime - starttime

