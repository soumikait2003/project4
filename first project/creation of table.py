import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='project'#put your database name
)
cur=mydb.cursor()
s="CREATE TABLE student(id int  not null UNIQUE,name varchar(20),marks int not null)"
#make changes according to you
cur.execute(s)
# to check table use commands
#1.SHOW TABLES
#2.DESC TABLES