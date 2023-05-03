class MyClass:
    def __init__(self,name): # create constructor
     self.name=name
# : The __init__() function is called automatically every time the class is being used to create a new object. 
cl=MyClass("Shubham")     
print(cl.name)