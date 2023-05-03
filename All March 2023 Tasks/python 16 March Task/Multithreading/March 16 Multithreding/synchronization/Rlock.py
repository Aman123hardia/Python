# The standard Lock object does not care which thread is currently holding that lock.If the lock is
# held and any thread attempts to acquire lock, then it will be blocked,even the same thread is
# already holding that lock.


# from threading import *
# l=Lock()
# print("Main Thread trying to acquire Lock")
# l.acquire()
# print("Main Thread trying to acquire Lock Again")
# l.acquire()


# from threading import *
# l=RLock()
# print("Main Thread trying to acquire Lock")
# l.acquire()
# print("Main Thread trying to acquire Lock Again")
# l.acquire()