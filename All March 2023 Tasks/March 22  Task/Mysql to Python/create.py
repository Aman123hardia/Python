import mysql.connector
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
)
database=mydatabase.cursor()
len1=''

#use Database in mysql 
def useDatabase():
 use=database.execute("use "+input("Enter which Database you want use "))

#create Database in mysql 
def createDatabase():
 len=int(input("How many Database you wanted to create ")) 
 for i in range(len):
   databaseName=input("Enter your Database Name ")
   database.execute("CREATE DATABASE "+databaseName)

#create table in mysql 
def createTable():
 len=int(input("How many Table you wanted to create ")) 
 for i in range(len):
    tableName=input("Enter your table Name ")
    len1=int(input("how many Column You wanted to add "))
    data=[]
    value=''
    column=''
    column=input("Enter Column Name ")
    value=input("which type of Data you insert Integer ,Varchar,float ")
    length=input("Enter the length of data ")
    database.execute("create table "+tableName+"("+column+" "+value+"("+length+")")
    data.clear()
    print(data)

 for j in range(len1-1):
    column=input("Enter Column Name ")
    value=input("which type of Data you insert Integer ,Varchar ,float")
    length=input("Enter the length of data ")
    data.append("Alter table "+tableName+" add column "+column+" " +value+"("+length+")")

 for index in data:
    database.execute(index)
    mydatabase.commit()

#Update data in mysql     
def updateData():
    tableName=input("Enter Table Name for Update")
    len=int(input("how many New Column You wanted to Update column "))
    data=[]
    value=''
    column=''
    for i in range(len):
        column=input("Enter Column Name ")
        value=input("Enter new value ")
        key=input("Enter the key name where you want to update ")
        keyValue=input("Enter the Key value which specify")
        data.append("Update "+tableName+" "+"set "+column+" = '" +value+"' where "+key+"="+" '"+keyValue+"'")
        
        print('\n_____________________________________________________________________\n')


    for index in data:
    # database.execute("UPDATE Employee SET firstName = 'Aman' WHERE id = '1'")
     database.execute(index)
     mydatabase.commit()

#drop database and table in mysql  
def drop():
 len=int(input("how many times you want to perform Drop operation")) 
 for i in range(len):
  dropName=input("what you wanted to Drop")
  if dropName=='Database' or dropName=='database':
   table=input("Enter Database Name")
   database.execute("Drop DATABASE "+table)
  elif dropName=='table' or dropName=='Table':
    table=input("Enter table Name")
    database.execute("Drop table "+table)
    
    
# insert into tables values    
def insert(*li):

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price) VALUES (%s, %s, %s) """

        record = (id, name, price)
        print(record)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")


        print("Failed to insert into MySQL table {}".format(error))


    