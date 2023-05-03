import mysql.connector
import requests,json
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)

data=requests.get('https://dummyjson.com/users')
dataList=json.loads(data.text)
database=mydatabase.cursor()
ke=[]

for index in range(len(dataList['users'])):
    if index<=20:
     for key in dataList['users'][index]:
         if key=='id' or key=='firstName' or key=='lastName' or key=='age' or key=='phone' or key=='username':
           ke.append(dataList['users'][index][key])
      
        
     da=(ke[0],ke[1],ke[2],ke[3])
     database.execute("INSERT INTO Employee VALUES(%s,%s,%s,%s)",da)
     mydatabase.commit()
     ke.clear() 

database.close()
