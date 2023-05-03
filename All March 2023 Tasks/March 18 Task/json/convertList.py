# import json
# li=["aman","shubham","nitesh","divyanshi","vinay"]       # list 
# jsonList='["aman","shubham","nitesh","divyanshi","vinay"]'  
# print(json.dumps(li))  #convert li to json return string of list
# print(type(json.loads(jsonList)))  #convert jsonList to python string return string of list


import json
tupleList=(1,2,3,4,5,6,7,8,9)     # list 
jsonTuple="(1,2,3,4,5,6,7,8,9)"
print(json.dumps(tupleList))  #convert li to json return string of list
print(type(json.loads(jsonTuple)))  #convert jsonList to python string return string of list