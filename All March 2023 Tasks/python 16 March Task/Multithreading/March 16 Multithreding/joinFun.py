# If a thread wants to wait until completing some other thread then we should go for join() method

from threading import Thread
import time 

def display():
    for i in range(10,1,-2):
        print("Thread 1")
        time.sleep(2)

t=Thread(target=display)
t.start()
t.join()         # join method stop the main thread when the running thread is not completed 

for i in range(10,1,-2):
    print("Thread 2")
        
        
 
 
 # join method  take one argument also is second 
from threading import Thread
import time 

def display():
    for i in range(10,1,-2):
        print("Thread 1")
        time.sleep(2)

t=Thread(target=display)
t.start()
t.join(4)         # join method stop the main thread when the running thread is not completed in second

for i in range(10,1,-2):
    print("Thread 2")