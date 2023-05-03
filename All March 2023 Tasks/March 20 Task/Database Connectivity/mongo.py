import pymongo

myclient = pymongo.MongoClient('mongodb+srv://amanhardia3366:Aman123@cluster0.d0uegiu.mongodb.net/?retryWrites=true&w=majority')
dblist = myclient.list_database_names()
print(type(myclient))

print("connection successfuly List of databses",dblist)
