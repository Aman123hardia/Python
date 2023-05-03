import mysql.connector
mydatabase=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Tout@53',
    database='mydatabase'
)

database=mydatabase.cursor()
def alterTable():
    len=int(input("how many New Column You wanted to add "))
    data=[]
    value=''
    column=''
    for i in range(len):
        column=input("Enter Column Name ")
        value=input("which type of Data you insert Integer ,Varchar ")
        length=input("Enter the length of data ")
        data.append("Alter table Employee add column "+column+" " +value+"("+(length)+")")
    print(data)

    for index in data:
        database.execute(index)
        mydatabase.commit()

    database.close()
