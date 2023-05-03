# We can use search() function to search the given pattern in the target string.
# If the match is available then it returns the Match object which represents first occurrence of the
# match.
# If the match is not available then it returns None

# import re
# s=input("Enter pattern to check: ")
# m=re.search(s,"aman")
# if m!= None:
#  print("Match is available")
#  print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
# else:
#  print("Match is not available")


# import re
# s="Learning Python is Very Easy"
# res=re.search("^Learn",s)
# if res != None:
#  print("Target String starts with Learn")
# else:
#  print("Target String Not starts with Learn")