# By default Main Thread is always non-daemon.But for the remaining threads Daemon nature will
# be inherited from parent to child.i.e if the Parent Thread is Daemon then child thread is also
# Daemon and if the Parent Thread is Non Daemon then ChildThread is also Non Daemon

from threading import *
def job():
 print("Child Thread")

t=Thread(target=job)
print(t.isDaemon())#False       
t.setDaemon(True)                  
print(t.isDaemon()) #True
