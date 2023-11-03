import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password ="root123",
database='project'#put your database name
)
cur=mydb.cursor()

query = "SELECT * FROM STUDENT where marks >=80  order by name desc"
# you can put your query
cur.execute(query)

myresult = cur.fetchall()

for x in myresult:# to print all the lines
	print(x)
mydb.close()
