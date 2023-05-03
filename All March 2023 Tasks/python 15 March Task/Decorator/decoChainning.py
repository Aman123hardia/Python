# Decorator chaining in python 
def car(func):
	def inner():
		x = func()
		return x+" or Car"
	return inner

def bike(func):
	def inner():
		x = func()
		return "I will go with bike"
	return inner

@car
@bike
def travel():
	return 'dont Go anywhere'

print(travel())
