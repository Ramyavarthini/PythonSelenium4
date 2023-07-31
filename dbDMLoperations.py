import mysql.connector

insert_query="insert into student values(105,'Ishana',75)"
update_query="update student set sname='Arjun' where sno=103"
delete_query="delete from student where sno=102"

try:  # to avoid any connection related issues, InterfaceError
    con=mysql.connector.connect(host='localhost',port=3306,user='root',password='root',database='mydb')
    curs=con.cursor() # establish connection through cursor.create cursor object. curser is temporary area
    curs.execute(delete_query)  # execute query through cursor
    con.commit()  #commit transaction
    con.close()
except:
    print("Connection Unsuccessfull")
print("Finished....")