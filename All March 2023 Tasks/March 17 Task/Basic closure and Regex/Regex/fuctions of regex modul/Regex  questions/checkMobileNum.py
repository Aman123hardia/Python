# 1. Every number should contains exactly 10 digits
# 2. The first digit should be 7 or 8 or 9


import re
n=input("Enter number:")
m=re.fullmatch("[7-9]\d{9}",n)
if m!= None:
 print("Valid Mobile Number",type(m))
else:
 print("Invalid Mobile Num")
 
 import re
n=input("Enter number:")
m=re.fullmatch("[7-9][0-9]{9}",n)
if m!= None:
 print("Valid Mobile Number",type(m))
else:
 print("Invalid Mobile Num")