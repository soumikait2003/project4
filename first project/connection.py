import mysql.connector                                                                  
mydb=mysql.connector.connect(host='localhost'
                             ,user='root'
                             ,password='root123')
print(mydb)
if(mydb):
    print("connection established")# checing for connection 
else:
    print("not established ")
cur=mydb.cursor()
cur.execute("CREATE DATABASE project")# put your own database name

#go to mysql client and put query SHOW DATABASES you can see the database