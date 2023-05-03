class Person:
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John")

del p1

try:
 print(p1)
except:
 print("Object does not exist")