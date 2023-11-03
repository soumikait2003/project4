import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='project'#put your database name
)
cur=mydb.cursor()
sql = "INSERT INTO STUDENT (id,name,marks )\
VALUES (%s, %s, %s)"
val = val = [("1","Nikhil",  "98"),#information entry
       ("2","Nisha",  "99"),
       ("3","Rohan",  "43"),
       ("4","Amit", "65"),
       ("5","Anil",  "45"), 
       ("6","Megha",  "55"), 
       ("7","Sita", "95")]
cur.executemany(sql,val)
mydb.commit() # to save the changes we are making
mydb.close()