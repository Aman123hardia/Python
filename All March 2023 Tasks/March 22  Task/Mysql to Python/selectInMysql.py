import mysql.connector
import requests,json
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)

mydata=mydatabase.cursor()
mydata.execute("""Select * from Amna""")
print(mydata.fetchall())
mydata.close()