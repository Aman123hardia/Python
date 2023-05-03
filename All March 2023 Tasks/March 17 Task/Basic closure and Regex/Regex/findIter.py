# Returns an Iterator object which yields Match object for every Matc

import re 
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("cabdabfsv")        
for match in matcher:
 count+=1
 print(match.start(),"...",match.end(),"...",match.group()) # start method give starting index
print("The number of occurrences: ",count)      
# end method give last index +1
#   group function give matching string