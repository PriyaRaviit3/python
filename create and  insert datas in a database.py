import pymysql

connection=pymysql.connect(host='localhost',user='root',password='i18n',db='college')

cursor=connection.cursor();

#cursor.execute("create database college")

#cursor.execute("create table students(name char(16),age INT(2),rollno INT(2))")

cursor.execute("insert into students(name,age,rollno)values('priya',27,1)")


connection.commit()


output:

name	age	rollno
priya	27	1