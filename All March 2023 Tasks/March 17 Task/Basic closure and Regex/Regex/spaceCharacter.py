# Pre defined Character classes:

# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .   Any character including special characters

# import re

# matcher=re.finditer("\s","a7b k@9z")       #Space placing check
#  for match in matcher:
#   print(match.start(),"......",match.group())
  


# import re
# matcher=re.finditer("\d","a7bk@9z")       #digit placing check
 
# for match in matcher:
#   print(match.start(),"......",match.group())


import re

matcher=re.finditer("\.","a7bk@9z")       #any character including placing check
for match in matcher:
  print(match.start(),"......",match.group())
  