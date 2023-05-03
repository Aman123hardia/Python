
class MyDecorator:
	def __init__(self, function):
		self.function = function
	
	def __call__(self):

		self.function()
    

@MyDecorator
def function():
	print("My function work properly")

function()
