
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
# convert json string to python object using load method
y = json.loads(x)

print(y["age"],y["name"],y["city"])
