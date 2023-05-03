import mysql.connector
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)
database=mydatabase.cursor()
tableName=input("Enter Table Name for Delete operation perform")
data=[]
value=''

column=input("What you wanted to Delete Row ,Column ,table")
if column=='Table' or column=='table':
  database.execute("Delete from "+tableName)
elif column=='column' or column=='Column':
 len=int(input("How many Column you wanted to delete"))  
 for i in range(len): 
  field=input("Enter which field name you wanted to know to delete")
  data.append("Alter table "+tableName+" Drop Column "+field)
  print('\n_____________________________________________________________________\n')
else:
 len=int(input("How many data you wanted to delete"))  
 for i in range(len): 
  field=input("Enter which field name you wanted to know to delete")
  keyValue=input("Enter the Key value which specify")
  data.append("Delete from "+tableName+" where "+field+"="+" '"+keyValue+"'")
  print('\n_____________________________________________________________________\n')


for index in data:
 database.execute(index)
 mydatabase.commit()

database.close()
