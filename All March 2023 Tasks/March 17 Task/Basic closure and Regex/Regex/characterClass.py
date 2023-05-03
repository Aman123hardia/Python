# We can use character classes to search a group of characters
# 1. [abc]===>Either a or b or c
# 2. [^abc] ===>Except a and b and c
# 3. [a-z]==>Any Lower case alphabet symbol
# 4. [A-Z]===>Any upper case alphabet symbol
# 5. [a-zA-Z]==>Any alphabet symbol
# 6. [0-9] Any digit from 0 to 9
# 7. [a-zA-Z0-9]==>Any alphanumeric character
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)


# import re
# matcher=re.finditer("x","a7b@k9zx") # check character place
# for match in matcher:
#   print(match.start(),"......",match.group())


# import re 
# matcher=re.finditer("[0-9]","a7b@k9zx")       # check numeric place 
# for match in matcher:
#   print(match.start(),"......",match.group())
  
  
  
# import re 
# matcher=re.finditer("[a-z]","a7b@k9zx")       # check alphabet  small albhabet space
# for match in matcher:
#   print(match.start(),"......",match.group())
