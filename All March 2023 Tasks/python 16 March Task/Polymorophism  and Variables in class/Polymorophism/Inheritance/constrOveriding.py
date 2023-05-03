# class P:
#   def __init__(self):
#    print('parent Constructor')
 
# class C(P):
#  pass

# C()     # parent class Constructor call


class P:
  def __init__(self):
   print('parent Constructor')
 
class C(P):
 def __init__(self):               # PARENT CLASS CONSTRUCTOR OVERIDE CHILD CLASS CONSTRUCTOR
   print('child Constructor')
 

C()  
 