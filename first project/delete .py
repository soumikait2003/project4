import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='project'#put your database name
)
cur=mydb.cursor()
s="delete from student where  marks<50"
mydb.commit()
