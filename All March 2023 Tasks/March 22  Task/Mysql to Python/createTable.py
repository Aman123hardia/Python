import mysql.connector
import requests,json
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)

database=mydatabase.cursor()
# table=database.execute("create table Employee(id int primary key)")

# insert=database.execute("Insert into Employee Values(1)")
# database.close()

database.execute("""INSERT INTO Employee(id) 
    VALUES (2)""")

database.execute("""Select * from Employee""")
print(database.fetchall())