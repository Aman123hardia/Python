import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.livemint.com/news/')

soup = BeautifulSoup(r.content, 'html.parser')
s= soup.findAll('a')

# print(s)

for line in s:
	print(line.text)
