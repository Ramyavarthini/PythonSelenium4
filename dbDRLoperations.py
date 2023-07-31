import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="mydb")  #localhost, there is no space
    curs=con.cursor()
    curs.execute("select * from student")
    for row in curs:
        print(row[0],row[1],row[2])
    con.close() # connection should be closed after the 'for loop'
except:
    print("Connection Unsuccessfull")
print("Finished...")