# Where we can declare Local variables:
# 1. Inside Instance Methods

# class LocalVariable:
#     def instanceMethod(self):
#         num=39           #Local  Variable   can not access outside of the class 
#         return num   
    

# inst=LocalVariable()
# print(inst.instanceMethod())



# 2. Inside Class Methods

# class LocalVariable:
#     @classmethod
#     def classMethod(cls): 
#      num=39           #Local  Variable  has very lower scope without it not possible to use
#      return num 
    

# print(LocalVariable.classMethod())



# 3. Inside Class Methods

class LocalVariable:
 @staticmethod
 def staticmethod(): 
   num=39           #Local  Variable  has very lower scope without it not possible to use
   return num 
    

print(LocalVariable.staticmethod())

