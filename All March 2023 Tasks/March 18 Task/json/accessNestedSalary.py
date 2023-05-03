import json

sampleJson ='''{
    "company":{
        "employee":{
            "salary":2000
        }
    }
}'''

data = json.loads(sampleJson)
print(data['company'])
print(data['company']['employee']['salary'])
