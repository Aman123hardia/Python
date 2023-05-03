# isAlive() method checks whether a thread is still executing or not.
from threading import *
import time
def thread1():
    for i in range(2):
     print("Thread 1")
     time.sleep(2)
     
def thread2():
    for i in range(2):
     print("Thread 2")
     time.sleep(1)
     
t1=Thread(target=thread1)
t2=Thread(target=thread2)

t1.start()
t2.start()

print(t1.is_alive())
print(t2.is_alive())