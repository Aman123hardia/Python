class P:                          # parent class
  x=10
  def property(self):
    print('I give all the thing Gold+Land+Cash+Power')
  
  def work(self):
   print('but you show work with My Company ')

class C(P):                        # child class all the property and behaviour present in child class
 
 def work(self):                   # method overriding change the implementation of parent class and use own method
  print('No I run own my buisness',self.x)

c=C()
c.property()
c.work()