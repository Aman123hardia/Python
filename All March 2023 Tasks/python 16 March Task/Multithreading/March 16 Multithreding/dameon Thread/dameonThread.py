# The threads which are running in the background are called Daemon Threads.
# The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main
# thread)
# Eg: Garbage Collector




from threading import current_thread

print(current_thread().isDaemon()) #False          isDaemon() method check the thread it daemon or not
print(current_thread().daemon) #False               daemon check the thread it daemon or not

try:
   print(current_thread().setDaemon(True)) #Fals    
except RuntimeError:
    print("cannot set daemon staus of active thread ..")





