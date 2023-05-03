import requests
from tabulate import tabulate
import json
from bs4 import BeautifulSoup
url='https://www.livemint.com/news/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('div', class_='headlineSec')
data=[]
dic=[]
fetch={}
link=[]
des=""
for i in s:
 for count,c in enumerate(i.stripped_strings):
   if count == 0 or count== 1 or count ==3:
    dic.append(c)
  
 else:
    link=list(i.find("a").get('href'))
    for i in range(5):
     link.pop(0) 
    str=""
    x=str.join(link)
    r = requests.get(url+x)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.findAll('div', class_='FirstEle')
    for k in s:
     des=k.find('p')
    
    data.append({"headings":dic[0],"Discription":des.text,"Reading Time":dic[1],"Uploaded Time":dic[2],"Links":url+x})
    link.clear()
    dic.clear()
    
      
with open("json_data.json", "w") as file1:
    file1.write(json.dumps(data ,indent=5))
















# for i in date:
#  print(date.text)
# content = s.find_all('h2')
# print(s)
# s1=[]
# for line in s:
#  s1.append(line.text.strip()+'\n')

# # for i in s1:
# #     print(i)

# dic={"headline":s1}
# print(dic["headline"])

# with open('json_data.json', 'w') as outfile:
#    for i in s1:
#     json.dumps({"headlines": i})
