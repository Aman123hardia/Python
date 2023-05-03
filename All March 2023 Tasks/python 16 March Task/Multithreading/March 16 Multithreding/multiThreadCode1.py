# Where ever a group of independent jobs are available, then it is highly recommended to
# execute simultaneously instead of executing one by one.For such type of cases we should go for
# Multi Threading.

# We can create a thread in Python by using 3 ways

# 1. Creating a Thread without using any class

# from threading import *
# def display():
#  for i in range(1,5):
#   print("  Child Thread",i)

# t=Thread(target=display)      #creating Thread object
# t.start()                     #starting of Thread
# for i in range(1,5): 
#  print("Main Thread",i)       # when multiple thread present then we can not expected 
 
 
 
 #2. Creating a Thread by extending Thread class
 
# from threading import *
# class MyThread(Thread):       # extend Thread class
#  def run(self):
#   for i in range(5):
#    print("Child Thread-1")
   
# t=MyThread()
# t.start()
# for i in range(5):
#  print("Main Thread-1")




#3 3. Creating a Thread without extending Thread class:

from threading import *
class Test:
 def display(self):
  for i in range(5):
   print("Child Thread-2")

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(5):
 print("Main Thread-2")