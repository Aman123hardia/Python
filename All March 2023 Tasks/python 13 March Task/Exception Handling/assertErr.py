# AssertionError with error_message.
x = 1
y = 1  
assert y != 0, "Invalid Operation"  #if condition is true return value
print(x / y)


# AssertionError with error_message.
x = 1
y = 0
assert y != 0, "Invalid Operation" # denominator can't be 0
print(x / y)