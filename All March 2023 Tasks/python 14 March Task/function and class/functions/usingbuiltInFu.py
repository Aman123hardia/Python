# filter(function,sequence)
# where function argument is responsible to perform conditional check
# sequence can be list or tuple or string.

# def isEven(x):
#   print(x)
#   if x%3==0:
#    return True
#   else:
#    return False

# l=[0,5,10,15,20,25,30]
# l1=list(filter(isEven,l))        # filter function
# print(l1) 



# For every element present in the given sequence,apply some functionality and generate
# new element with the required modification. For this requirement we should go for
# map() function.

# l=[1,2,3,4,5]
# def d(x):
#  return x
# l1=list(map(d,l))
# print(l1) #[2, 4, 6, 8, 10]

# Map using lambada function
# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)



# reduce() function reduces sequence of elements into a single element by applying the
# specified function.
# reduce(function,sequence)
# reduce() function present in functools module and hence we should write import
# statement.


# from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)  
# print(result) # 150