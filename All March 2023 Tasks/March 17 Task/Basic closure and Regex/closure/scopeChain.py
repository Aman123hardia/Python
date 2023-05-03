
def sum(a) :
  return lambda b:lambda c : lambda d : a+b+c+d
 
s=sum(10)
t=s(20)
u=t(30)
v=u(40)
print(v)

# scope chain of closure function