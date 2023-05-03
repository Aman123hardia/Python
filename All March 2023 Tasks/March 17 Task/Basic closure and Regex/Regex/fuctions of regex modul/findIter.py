# Returns the iterator yielding a match object for each match.
# On each match object we can call start(), end() and group() functions.

import re

itr=re.finditer("[a-z]","a7b9c5k8z")
for m in itr:
 print(m.start(),"...",m.end(),"...",m.group())