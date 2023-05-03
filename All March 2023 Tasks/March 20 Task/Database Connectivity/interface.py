import zope.interface


class BaseI(zope.interface.Interface):
	def m1(self, x):
		pass
	def m2(self):
		pass

class DerivedI(BaseI):
	def m3(self, x, y):
		pass

@zope.interface.implementer(DerivedI)
class cls:
	def m1(self, z):
		return z**3
	def m2(self):
		return 'foo'
	def m3(self, x, y):
		return x ^ y
	
# Get base interfaces
print(DerivedI.__bases__)

# Ask whether baseI extends
# DerivedI
print(BaseI.extends(DerivedI))

# Ask whether baseI is equal to
# or is extended by DerivedI
print(BaseI.isEqualOrExtendedBy(DerivedI))

# Ask whether baseI is equal to
# or extends DerivedI
print(BaseI.isOrExtends(DerivedI))

# Ask whether DerivedI is equal
# to or extends BaseI
print(DerivedI.isOrExtends(DerivedI))
