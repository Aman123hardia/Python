import pymongo

myclient = pymongo.MongoClient('mongodb+srv://amanhardia3366:Aman123@cluster0.d0uegiu.mongodb.net/?retryWrites=true&w=majority')
dblist = myclient.list_database_names()
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "2": {"$regex": "^A"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted")
