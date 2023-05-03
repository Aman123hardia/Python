# The main objective of decorator functions is we can extend the functionality of existing
# functions without modifies that function.

# def chat(name):
#  print("Hello",name,"you are online")  #Normal function so make change the message using decorator of fun
 
# chat("Aman")


def decor1(func):          # decor function 
	def inner(n):
		x = func(n)
		return x * x
	return inner

@decor1
def num(n):         #without changing
	return n           



# print(num(2))       