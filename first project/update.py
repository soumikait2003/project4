import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='project'#put your database name
)
cur=mydb.cursor()
s="update student set  marks=marks+10 where marks<50"
cur.execute(s)
mydb.commit() 