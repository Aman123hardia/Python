# If multiple threads are executing simultaneously then there may be a chance of data inconsistency
# problems.

# from threading import *
# import time
# def wish(name):
#   for i in range(5):
#    print("",end='')
#    time.sleep(1)
#    print(name)

# t1=Thread(target=wish,args=("parent",))         
# t2=Thread(target=wish,args=("child",))
# t1.start()
# t2.start()                                 #inconsistency output so we use synchronization


# The Lock object can be hold by only one thread at a time.If any other thread required the same
# lock then it will wait until thread releases lock


from threading import *
l=Lock()
l.acquire()          # this acquired the lock, all subsequent attempts to acquire the                 
#lock are blocked until it is released
print(type(l))
l.release()