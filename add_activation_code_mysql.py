import mysql.connector
from generateActivationCode import generateActivationCode
def save_code():
    try:
        conn = mysql.connector.connect(user='root',password='123',database='test')
        cursor = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            codelist = generateActivationCode(1)
            cursor.execute('''CREATE TABLE IF NOT EXISTS CODE(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                           )''')
            for code in codelist:
                str1 = "insert into code(code) values('%s')" %code
                print str1
                cursor.execute("insert into code(code) values('%s')" %code)

                conn.commit()
        except BaseException as e:
            print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    save_code()



