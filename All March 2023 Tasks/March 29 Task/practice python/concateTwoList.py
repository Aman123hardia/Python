# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# list3= [i + j for i, j in  zip(list1,list2)]

    
# print(list3)


#conctate 1 list of item  with 2 list of 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
con=[x+y for x in list1 for y in list2]
print(con)
