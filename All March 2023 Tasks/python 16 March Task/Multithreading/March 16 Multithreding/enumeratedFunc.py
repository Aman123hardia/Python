# This function returns a list of all active threads currently running.
from threading import *
import time
def display():
 print(current_thread().getName(),"...started")
 time.sleep(2)

t1=Thread(target=display,name="Thread1")
t2=Thread(target=display,name="Thread2")
t3=Thread(target=display,name="Thread3")
t1.start()
t2.start()
t3.start()

l=enumerate()
for t in l:
 print("Thread Name:",t.name)
 time.sleep(2)
