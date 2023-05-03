# simple nested function
def greet(name):
    def display_name():
        print("Hi", name)
    display_name()

greet("John")         #nested function 


# Python closure is a nested function
# that allows us to access variables of the outer
# function even after the outer function is closed.


def greet(name):        #closure function 
    def display_name():
     return   "Hi "+name
    return display_name

closure=greet("aman")

print(closure())