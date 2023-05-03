import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://www.livemint.com/news/')

soup = BeautifulSoup(r.content, 'html.parser')
s= soup.findAll('a')

for link in soup.find_all('a',attrs={'href': re.compile("^https://")}):
 for line in s:
  if line.text=="Latest":
   print(link.text)

    

	  