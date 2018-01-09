import pymysql
import xlsxwriter
conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='bg6mgd',db='1',charset='UTF8')
cursor = conn.cursor()
cursor.execute("select* from customers")
data=cursor.fetchone()
while data:
    for i in data:
        print(i)
    data=cursor.fetchone()
cursor.close()
conn.close()
