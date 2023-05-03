from threading import *
s=Semaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("End")

# It is valid because in normal semaphore we can call release() any number of times.


# BounedSemaphore is exactly same as Semaphore except that the number of release() calls should
# not exceed the number of acquire() calls,otherwise we will get

from threading import *
s=BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("End")


# Note: To prevent simple programming mistakes, it is recommended to use BoundedSemaphore
# over normal Semaphore.