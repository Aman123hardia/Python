import requests
r = requests.get('https://www.freepressjournal.in/')

print(r.content)   #content of this url
print(r.url)          #fetch url
print(r.status_code)      # check status
