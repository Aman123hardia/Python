# Where we can declare Staic variables:

#1] In general we can declare within the class directly but from out side of any method

# class StaticVariable:
#   name="Aman"       

# print(StaticVariable.name)



# 2. Inside constructor by using class name

# class StaticVariable:
#   def __init__(self):
#     StaticVariable.name="Aman"       

# print(StaticVariable().name)


# 3. Inside instance method by using class name

# class StaticVariable:
#   def classVariable(self):
#     StaticVariable.name="Aman" 
#     return self.name      

# print(StaticVariable().classVariable())



# 4. Inside classmethod by using either class name or cls variable

# class StaticVariable:
#   @classmethod
#   def classMethod(cls):
#     cls.name="Aman" 

# StaticVariable.classMethod()
# print(StaticVariable.name)



# 5.inside static method: by using classname

# class StaticVariable:
#   @staticmethod
#   def staticMethod():
#     StaticVariable.name="Pavan" 

# StaticVariable.staticMethod()
# print(StaticVariable.name)




#6] From outside of class: by using either object reference or classname
# class StaticVariable:
#   pass
# StaticVariable.name="Shankar"
# print(StaticVariable.name)



# with the help del keyword we delete instance variable
class DelStaticVariable:
 num=50
 
print(DelStaticVariable.num)
del DelStaticVariable.num       
print(DelStaticVariable.num) # Error after deleting the static variable