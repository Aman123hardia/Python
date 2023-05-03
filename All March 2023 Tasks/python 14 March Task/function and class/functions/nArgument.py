# def sum(*n): # store as a tuple
#  total=0
#  for n1 in n:
#   total=total+n1
#  print("The Sum=",total)
#  return n

# sum()
# sum(10)
# sum(10,20)
# print(type(sum(10,20,30,40)))      # return type tupe



def f1(*s,n1):
 for s1 in s:
  print(s1)
 print(n1)
f1("A","B",n1=10)  # by keword argument we can use also this type of n argrument

