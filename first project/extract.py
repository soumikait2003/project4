import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='db1'
)
cur=mydb.cursor()
s="SELECT * FROM student"
cur.execute(s)
res=cur.fetchall()
for i in res:
    print(i)