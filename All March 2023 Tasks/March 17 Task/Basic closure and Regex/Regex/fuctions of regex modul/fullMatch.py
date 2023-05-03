# We can use fullmatch() function to match a pattern to all of target string. i.e complete string
# should be matched according to given pattern.
# If complete string matched then this function returns Match object otherwise it returns None


import re
s=input("Enter pattern to check: ")
m=re.fullmatch(s,"ababab")
if m!= None:
 print("Full String Matched")
else:
 print("Full String not Matched")