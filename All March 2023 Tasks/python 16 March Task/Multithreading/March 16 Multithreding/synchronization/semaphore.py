# Semaphore can be used to limit the access to the shared resources with limited capacity.
# Semaphore is advanced Synchronization Mechanism.

# Case-1:
# s=Semaphore()
# In this case counter value is 1 and at a time only one thread is allowed to access. It is exactly same
# as Lock concept.
# Case-2: s=Semaphore(3)
# In this case Semaphore object can be accessed by 3 threads at a time.The remaining threads have
# to wait until releasing the semaphore

#with the help of semaphone we can fix how many thread acquire the thread
from threading import *
import time
s=Semaphore(2)
def wish(name):
 s.acquire()
 for i in range(10):
  print("Good Evening:",end='')
  time.sleep(2)
  print(name)
  s.release()

t1=Thread(target=wish,args=("Dhoni",))
t2=Thread(target=wish,args=("Yuvraj",))
t3=Thread(target=wish,args=("Kohli",))
t4=Thread(target=wish,args=("Rohit",))
t5=Thread(target=wish,args=("Pandya",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()