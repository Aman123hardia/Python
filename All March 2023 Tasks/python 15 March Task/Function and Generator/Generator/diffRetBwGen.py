def useReturn():
    return 10
    print("Hello")
    # It exits a function and returns a value to its caller after return data will loss.
    
print(useReturn())


def inGen(): 
 yield  2
 yield  1
#  The code written after the yield statement is executed in the following function call.
g=inGen()
print(next(g))
print(next(g))
