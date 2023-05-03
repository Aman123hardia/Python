# In python method overloading is not possible
# But in Python Method overloading is not possible.
# If we are trying to declare multiple methods with same name and different number of arguments
# then Python will always consider only last method.

# class Test:
#  def method1(self,a):
#   print('method1 ',a)
  
#  def method2(self,a,b):
#     print('method2',a,b)

# Test().method2(2,3)
# Test().method2(2)        #if we try one parameter then give error typeerror one missing argument


# Method overload with Default Arguments:
# class Test:
#  def method1(self,a=None,b=None,c=None):
#   print('Constructor with 0|1|2|3 number of arguments',a,b,c)

# t1=Test()
# t2=Test(10)
# t3=Test(10,20)
# t4=Test(10,20,30)



# Method overload with Variable Number of Arguments:
# class Test:
#  def __init__(self,*li):
#   print('Constructor with 0|1|2|3 number of arguments',li)

# t1=Test()
# t2=Test(10)
# t3=Test(10,20)
# t4=Test(10,20,30)
# t4=Test(10,20,30,32,34,345,345,345,)
