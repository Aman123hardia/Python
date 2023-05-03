# Write a python program to check whether the given string is Java
# language identifier or not?

# 1. The allowed characters are a-z,A-Z,0-9,#
# 2. The first character should be a lower case alphabet symbol from a to k
# 3. The second character should be a digit divisible by 3
# 4. The length of identifier should be atleast 2

import re
s=input("Enter Identifier:")
m=re.fullmatch("[a-z][0369][a-zA-Z0-9#]*",s)
if m!= None:
 print(s,"is valid Java Identifier")
else:
 print(s,"is invalid Java Identifier")