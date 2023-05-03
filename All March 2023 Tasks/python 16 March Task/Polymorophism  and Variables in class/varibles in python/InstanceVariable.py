# Where we can declare Instance variables:
# 1. Inside Constructor by using self variable

# class InstanceVariable:
#     def __init__(self,name):
#         self.name=name       #instance Variable       
    

# inst=InstanceVariable("aman")
# print(inst.name)



# 2. Inside Instance Method by using self variable

# class InstanceVariable:
#     def instanceMethod(self,name): 
#         self.name=name               #Inside Instance Method instance Variable
             
    

# inst=InstanceVariable()
# inst.instanceMethod("shankar")
# print(inst.__dict__)                #The __dict__ in Python represents a dictionary #or any mapping object that is used to store the attributes of the object. 



# 3. Outside of the class by using object reference variable


# class InstanceVariable:
#    def getName(self):
#        print(self.name) 
            
             
# inst=InstanceVariable()
# inst.name="Aman"           #Outside of class by using object refra
# # print(inst.__dict__)
# inst.getName()  


# with the help del keyword we delete instance variable


class DelInstance:
  def __init__(self):
      self.num=50

insOb=DelInstance()
print(insOb.__dict__)
del insOb.num         
print(insOb.__dict__)