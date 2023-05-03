# Web Scraping by using Regular Expressions:

import re,urllib,urllib.request
sites="variety".split()
print(sites)
for s in sites:
 print("Searching...",s)
u=urllib.request.urlopen("http://"+s+".com")
text=u.read()
title=re.findall("<title>.*</title>",str(text))
print(title[0])