import pymongo

myclient = pymongo.MongoClient('mongodb+srv://amanhardia3366:Aman123@cluster0.d0uegiu.mongodb.net/?retryWrites=true&w=majority')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop() 