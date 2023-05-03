# for x in "banana": 
#   print(x) 
  
fruits = ["apple", "banana", "cherry"]      
# print(fruits[2])
# for x in fruits:
#   if x=="apple":
#    print(x) 
  
# i = 1
# while i < 6:
#   print(i,end='')
#   i += 1
  
  
  
# fruits = {"apple", "banana", "cherry"}   # set example
# if "apple" in fruits:
#   print("Yes, apple is a fruit!")
  
  # add more items by update method 
  # remove method to  remove items to set == it arise an error if item is not found 
  # add method add item in to set list 
  # discard method does not arise an error if not found
    
# fruits = {"apple", "banana", "cherry"} 
# fruits.discard("apple")
# print(fruits)




# list is one dimensional array

list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))

print(len(list2))


# touples 
tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))






list1=[1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2=[2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,2)) # returns the index value of the element from the particular start position given


tuple1=(1,3,6,7,9,10)
print(tuple1.index(6))
print(tuple1.index(9))


set1={1,5,6,3,9}
# set1.index()  will throw an error as they are unordered


dict1={"key1":"value1","key2":"value2"}
# dict1.index("key1") will throw an error
print(dict1.get("key1"))
