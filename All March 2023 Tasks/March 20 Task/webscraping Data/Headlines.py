import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.livemint.com/news/')

soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('h2', class_='headline')
# content = s.find_all('h2')
# print(s)
s1=[]
for line in s:
	s1.append(line.text)

for line1 in s1:
    print(line1, end="")