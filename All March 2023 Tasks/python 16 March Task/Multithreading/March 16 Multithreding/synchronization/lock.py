from threading import *
import time
l=Lock()
def wish(name):
 l.acquire()                   # acquire lock thread relase when they are completed
 for i in range(3):
  print("Good Evening:",end='')
  time.sleep(2)
  print(name)
 l.release()

t1=Thread(target=wish,args=("shiv",)) 
t2=Thread(target=wish,args=("shivay Mo",))      
t3=Thread(target=wish,args=("shivay Riko",))
t1.start()
t2.start()
t3.start()