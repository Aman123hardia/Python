import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.freepressjournal.in/')
print(r)


soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
