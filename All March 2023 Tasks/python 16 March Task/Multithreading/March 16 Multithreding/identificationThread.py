from threading import *
def test():
 print("Child Thread")

t=Thread(target=test)
t.start()
print("Main Thread identification Number: -",current_thread().ident)
print("Child Thread identification Number:-",t.ident)