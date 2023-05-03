# We can use match function to check the given pattern at beginning of target string.
# If the match is available then we will get Match object, otherwise we will get None.

import re
s=input("Enter pattern to check: ")
m=re.match(s,"abcabdefg")

if m!= None:
 print("Match is available at the beginning of the String")
 print("Start Index:",m.start(), "and End Index:",m.end())      #show match index and ending index+1
else:
 print("Match is not available at the beginning of the String")