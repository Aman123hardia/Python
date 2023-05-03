# Python program showing
# abstract base class work

from abc import ABC,abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):
	
 def aman(self):
    print("Hello")


# Driver code
R = Triangle()
R.noofsides()

