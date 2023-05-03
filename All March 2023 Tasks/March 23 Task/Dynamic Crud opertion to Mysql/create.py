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
 data=input("Enter which Database you want use = ")
 database.execute("use "+data)
 print("Now you are using "+data+" database")

#create Database in mysql 
def createDatabase():
   databaseName=input("Enter your Database Name = ")
   database.execute("CREATE DATABASE "+databaseName)
   print("You are successfully created "+databaseName+" database")

#create table in mysql 
def createTable():
 tableName=input("Enter your table Name = ")
 len1=int(input("how many Column You wanted to add = "))
 data=[]
 value=''
 column=''
 column=input("Enter Column Name = ")
 value=input("which type of Data you insert Integer ,Varchar,float = ")
 length=input("Enter the length of data = ")
 
 database.execute("create table "+tableName+"("+column+" "+value+"("+length+")"+")")
 data.clear()
 print(data)

 for j in range(len1-1):
    column=input("Enter Column Name = ")
    value=input("which type of Data you insert Integer ,Varchar ,float = ")
    length=input("Enter the length of data = ")
    data.append("Alter table "+tableName+" add column "+column+" " +value+"("+length+")")

 for index in data:
    database.execute(index)
    mydatabase.commit()
 print("You are successfully created "+tableName+" table ")
#Update data in mysql     
def updateData():
    tableName=input("Enter Table Name for Update = ")
    len=int(input("how many New Column You wanted to Update column = "))
    data=[]
    value=''
    column=''
    for i in range(len):
        column=input("Enter Column Name = ")
        value=input("Enter new value = ")
        key=input("Enter the key name where you want to update = ")
        keyValue=input("Enter the Key value which specify = ")
        data.append("Update "+tableName+" "+"set "+column+" = '" +value+"' where "+key+"="+" '"+keyValue+"'")
        
        print('\n_____________________________________________________________________\n')


    for index in data:
     database.execute(index)
     mydatabase.commit()
    
    print("You are successfully Update "+tableName+" table Data ")

#drop database and table in mysql  
def drop():
  dropName=input("what you wanted to Drop = ")
  if dropName=='Database' or dropName=='database':
   table=input("Enter Database Name = ")
   database.execute("Drop DATABASE "+table)
   print("You are successfully Drop Database "+dropName) 
  elif dropName=='table' or dropName=='Table':
    table=input("Enter table Name = ")
    database.execute("Drop table "+table)
    print("You are successfully Drop table "+dropName) 

def show():
  show=input("what you wanted see table or database = ")
  if show=='Database' or show=='database':
   database.execute("show databases ")
   print(database.fetchall())
  elif show=='table' or show=='Table':
    database.execute("show tables ")
    print(database.fetchall())
#select data and table in mysql    
def select():
  table=input("Enter table  name = ")
#   data=input("what you want to see particular data enter = p or all record = * ")
#   if data=='p' or data=='P':
#     li=[]
#     exe='select ' 
#     while True:
#         li.append(input("Enter column Names = ")) 
#         data=input("if you do not add press E = ")
#         if data=='e' or data=='E':
#           break
#     for i in li:
#         exe+=i+','
#     query=exe[0:-2]
#     exe=exe[:len(exe)-2]=" from"+table
#     print(exe,query)
#     exit()
#     database.execute(exe)
#     print(database.fetchall())
#   else:
  database.execute("select * from "+table)
  print(database.fetchall())
    
    


    