# sub means substitution or replacement
# re.sub(regex,replacement,targetstring)
# In the target string every matched pattern will be replaced with provided replacement.

import re
s=re.sub("[0-9]","*","a7b9c5k8z")
print(s)