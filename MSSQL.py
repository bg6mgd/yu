import pymssql
import xlsxwriter
workbook = xlsxwriter.Workbook('sqL2.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
server = '127.0.0.1'
user = 'sa'
password = 'bg6mgd'

conn = pymssql.connect(server, user, password, "JZWRZS")
cursor = conn.cursor()
cursor.execute('select name from syscolumns where id=object_id(\'zh_st_zdczb\')')
zdrow=cursor.fetchone()
while zdrow:
    for zd in zdrow:
        worksheet.write(row,col,zd)
        print(zd)
        zdrow=cursor.fetchone()
        col+=1
col=0
row=1  
cursor.execute('SELECT * FROM zh_st_zdczb WHERE ID<10000')
srow = cursor.fetchone()

while srow:
    for r in srow:
        worksheet.write(row,col,r)
        col+=1
    col=0
    row+=1
    srow = cursor.fetchone()
workbook.close()
conn.close()
