# import threading      # with the help of threading module we can create own thread  and see current thread
# print("Current Executing Thread:",threading.current_thread().getName()) 

# # Every Python Program by default contains one thread which is nothing but MainThread.
from threading import *
print(current_thread().name)
