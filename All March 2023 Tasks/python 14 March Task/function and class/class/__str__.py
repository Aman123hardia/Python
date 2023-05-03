import datetime

mydate = datetime.datetime.now()

print("__str__() string: ", mydate.__str__())
print("str() string: ", str(mydate))

# The __str__() method returns a human-readable, or informal
# , string representation of an object. This method is called
# by the built-in print() , str() , and format() functions. If you don't define a __str__() method for a class, 
# then the built-in object implementation calls the __repr__() method instead.


print("__repr__() string: ", mydate.__repr__())
print("repr() string: ", repr(mydate))


# The __repr__() method returns a more information-rich, or official, 
# string representation of an object. This method is called by the built-in repr() function. If possible, the string returned should be a valid Python expression that can be used to recreate the object.
# In all cases, the string should be informative and unambiguous.

