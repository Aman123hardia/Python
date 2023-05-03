import mysql.connector
import requests,json
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)

database=mydatabase.cursor()


data=requests.get('https://dummyjson.com/users')
dataList=json.loads(data.text)
database=mydatabase.cursor()

for index in range(len(dataList['users'])):
    if index<=20:
     for key in dataList['users'][index]:
        if key=='firstname' or key=='lastName' or key=='phone':
         database.execute("ALTER TABLE Employee \ADD (%s)"% dataList[index][key]+"VARCHAR(100)")
        elif key=='address' or key=='age':
         database.execute("ALTER TABLE Employee \ADD (%s)"% dataList[index][key]+"int(100)")