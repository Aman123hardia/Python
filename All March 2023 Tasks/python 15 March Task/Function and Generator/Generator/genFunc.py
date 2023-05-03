# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values.

def mygen():  # it store in global fram
 yield 'A'
 yield 'B'
 yield 'C'
 
g=mygen()

print(type(g)) # if we use yield in normal function then it convert genrator function

print(next(g))
print(next(g))
print(next(g)) # stop iteration
# print(next(g)) # give error