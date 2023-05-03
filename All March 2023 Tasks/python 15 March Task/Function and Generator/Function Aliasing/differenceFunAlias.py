# What is the differenece between the following lines?
# f1 = outer
# f2 = outer()

def fun():
   print("hello")
   
f1=fun  
print(f1) #function address
# In the first case for the outer() 
#function we are providing another name f1(function aliasing).

f2=fun()
print(f2) # return function 