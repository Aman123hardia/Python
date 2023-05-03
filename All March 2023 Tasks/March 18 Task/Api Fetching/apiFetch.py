import requests
import json
file=open('jsonData.txt','w')

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://dummyjson.com/quotes')

#print the response text (the content of the requested file):
print(x.status_code)                 # 1 response get code
# print(x.text)                        # 2 get data from api
data=json.loads(x.text)      # 3 Parse the data into JSON format
print(data)