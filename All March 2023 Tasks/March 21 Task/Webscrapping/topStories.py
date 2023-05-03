import requests
from bs4 import BeautifulSoup

url='https://www.bbc.com/news'
response = requests.get(url)
s=set()
print(type(s))
soup = BeautifulSoup(response.text, 'html.parser')
# headlines = soup.find('body').find_all('h3')
# for i in headlines:
#     print(i.text)
    
containers = soup.find('div', {'id': 'news-top-stories-container'})
data=set()
paragraph=containers.findAll('h2')
length=len(containers.findAll('h2'))
for i in range(length):
    data.add(paragraph[length-1])


print(len(data))

for i in data:
 print(i.text)