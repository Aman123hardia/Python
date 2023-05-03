import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="sys",
  password="Tout@53"

)
data=mydb.cursor()
print(mydb) 