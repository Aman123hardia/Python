# In python constructor overloading is not possible
# If we are trying to declare multiple constructors with same name and different number of arguments
# then Python will always consider only last constructor.

class Test:
 def __init__(self,a):
  print('constructor1 ',a)
  
 def __init__(self,a,b):
    print('constructor2...',a,b)

Test(2,3)
# Test()                       #if we try one parameter then give error type error one missing argument


# constructor overload with Default Arguments:
# class Test:
#  def __init__(self,a=None,b=None,c=None):
#   print('Constructor with 0|1|2|3 number of arguments',a,b,c)

# t1=Test()
# t2=Test(10)
# t3=Test(10,20)
# t4=Test(10,20,30)



# constructor overload with Variable Number of Arguments:
# class Test:
#  def __init__(self,*li):
#   print('Constructor with 0|1|2|3 number of arguments',li)

# t1=Test()
# t2=Test(10)
# t3=Test(10,20)
# t4=Test(10,20,30)
# t4=Test(10,20,30,32,34,345,345,345,)




# n Argument of send to constructor store as a dictionay
class Test:
 def __init__(self,**li):
  print('Constructor ',li)

t1=Test()
t2=Test(n=10)
t3=Test(n1=10,n2=20)

