# importing modules
import urllib.request
from bs4 import BeautifulSoup

# providing url
url = "https://www.livemint.com/news/"

# opening the url for reading
html = urllib.request.urlopen(url)

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')

# getting all the paragraphs
for para in htmlParse.find_all("p"):
	print(para.get_text())



# for para in htmlParse.find_all("span"):
# 	print(para.get_text())
 
# for para in htmlParse.find_all("li"):
#  if   para.get_text()=='How layoffs in US tech giants benefit India? G...':
#      print(para.content)
 