class Person:
  def __init__(self):
    self.name = name
#   The self parameter is a reference to the current instance of the class, 
#   and is used to access variables that belong to the class.

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person(input("Enter your Name = "))
p1.myfunc() 