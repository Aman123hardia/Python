#operator overloading happen in 2 thing by us in + and * operator
# Eg1: + operator can be used for Arithmetic addition and String concatenation

# print(10+20) #30   and sum of num
# print('durga'+'soft') #durgasoft string concate


# Eg2: * operator can be used for multiplication and string repetition purposes.
# print(10*20)#200
# print('durga\n'*10)#durgadurgadurga

# __add__ method  call when overload
# class Book:
#  def __init__(self,pages):
#   self.pages=pages
#  def __add__(self,other):         # __add__ method  call when overload
#   return self.pages+other.pages

# b1=Book(100)
# b2=Book(200)
# print('The Total Number of Pages:',b1+b2)



#greater and less than operator

class Student:
 def __init__(self,name,marks):
  self.name=name
  self.marks=marks
 def __gt__(self,other):
  print("Heloo")
  return self.marks>other.marks
 def __le__(self,other):
  return self.marks<=other.marks


s1=Student("Durga",100)
s2=Student("Ravi",200)
print("s1<=s2 =" ,s1<=s2)
print("s1>=s2 =",s1>=s2)



# this method help to overload the data
#     + ---> object.__add__(self,other)
#     - ---> object.__sub__(self,other)
#     * ---> object.__mul__(self,other)
#     / ---> object.__div__(self,other)
#     // ---> object.__floordiv__(self,other)
#     % ---> object.__mod__(self,other)
#     ** ---> object.__pow__(self,other)
#     += ---> object.__iadd__(self,other)
#     -= ---> object.__isub__(self,other)
#     *= ---> object.__imul__(self,other)
#     /= ---> object.__idiv__(self,other)
#     //= ---> object.__ifloordiv__(self,other)
#     %= ---> object.__imod__(self,other)
#     **= ---> object.__ipow__(self,other)
#     < ---> object.__lt__(self,other)
#     <= ---> object.__le__(self,other)
#     > ---> object.__gt__(self,other)
#     >= ---> object.__ge__(self,other)