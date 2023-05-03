import json
# input dictionary
dict = {
   "id": ("1", "2", "3"),
   "languages": ("python", "java", "c++"),
   "authors": ("abc", "xyz", "pqr")
}
# converting dictionary of tuples into json
result = json.dumps(dict ,indent=1)
# printing the resultant json
print(result)
