
from bs4 import BeautifulSoup
import requests
import re
def getHTMLdocument(url):
	response = requests.get(url)
	return response.text

url_to_scrape = "https://www.livemint.com/news/"
html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

for link in soup.find_all('a',
						attrs={'href': re.compile("^https://")}):
	# display the actual urls
	print(link.get('href'))
