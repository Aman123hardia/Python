import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Tout@53"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")