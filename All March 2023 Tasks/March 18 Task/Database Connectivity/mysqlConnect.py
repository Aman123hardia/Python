import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='Tout@53',
         host='127.0.0.1',
         database='mysql')

conn.close()