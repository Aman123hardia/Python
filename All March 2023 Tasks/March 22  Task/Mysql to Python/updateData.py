import mysql.connector
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)
database=mydatabase.cursor()
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

database.close()
