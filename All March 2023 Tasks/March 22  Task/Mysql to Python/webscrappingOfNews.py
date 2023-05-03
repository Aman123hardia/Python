
import requests,time,json
from rich.console import Console
from rich.table import Table
from rich.progress import track
from bs4 import BeautifulSoup
from datetime import date

data,dic,link=[],[],[]
fetch={}

today = str(date.today())
url='https://www.livemint.com/news/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('div', class_='headlineSec')


for i in track(s ,description="Process data will be loading ....."):
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
    s = soup.find_all('div', class_='FirstEle')
    des=soup.find('p')
    time.sleep(0.1)
    data.append({"headings":dic[0],"Discription":des.text.strip(),"Reading Time":dic[1],"Uploaded Time":dic[2],"Links":url+x})
    link.clear()
    dic.clear()
    
      
with open("json_data.json", "w") as file1:
    file1.write(json.dumps(data ,indent=5))

with open("json_data.json", "r") as file1:
  dic=  json.loads(file1.read())
   
table = Table(title="Today Headlines "+today)
table.add_column("Uploaded Time", style="yellow")
table.add_column("Reading Time", style="green")
table.add_column("headlines", justify="left", style="cyan")
table.add_column("Description", justify="left", style="blue")
table.add_column("Links", justify="left", style="white")

for index,i in enumerate(dic):
  table.add_row( dic[index]['Uploaded Time'],dic[index]['Reading Time'],dic[index]['headings'],dic[index]['Discription'],dic[index]['Links'])

console = Console()
console.print(table)