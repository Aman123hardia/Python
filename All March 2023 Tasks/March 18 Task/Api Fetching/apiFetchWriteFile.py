import requests
r = requests.get('https://dummyjson.com/quotes')


with open('events.py','w') as fd:
    fd.write(r.text)
    
with open('events.py','r') as fd:
    print(fd.read())