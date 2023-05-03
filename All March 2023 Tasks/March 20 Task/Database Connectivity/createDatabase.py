import pymongo

myclient = pymongo.MongoClient('mongodb+srv://amanhardia3366:Aman123@cluster0.d0uegiu.mongodb.net/?retryWrites=true&w=majority')
dblist = myclient.list_database_names()
print("Before creation of database ",dblist)
dataBase=myclient['pythonWork']


# create collection 
collect=dataBase['showFile']
print(collect) 