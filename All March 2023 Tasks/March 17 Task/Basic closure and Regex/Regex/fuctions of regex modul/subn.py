# It is exactly same as sub except it can also returns the number of replacements.
# This function returns a tuple where first element is result string and second element is number of
# replacements.
# (resultstring, number of replacements)


import re
t=re.subn("[a-z]"," ","a7b9c5k8z")
print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])


import re
t=re.subn("[a-z]","*","a7b9c5k8z")
print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])