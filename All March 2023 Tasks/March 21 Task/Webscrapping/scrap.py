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
    
containers = soup.find_all('a', {'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'})
container = containers[0]
print(url)
print(url.lstrip('news'))
linktag = list(container.get('href'))
for i in range(5):
 linktag.pop(0)


x="".join(linktag)
print(x)
# url.container.get('href')

response = requests.get("https://www.bbc.com/news/world-europe-65021987")
soup = BeautifulSoup(response.text, 'html.parser')
containers = soup.find('header', {'class': 'ssrcss-1eqcsb1-HeadingWrapper e1nh2i2l5'})
s=set()
for i in containers:
  print(containers.text)