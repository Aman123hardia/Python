from threading import *

import time
def doubles(numbers):
 for n in numbers:
  time.sleep(1)
  print(n," number Double to =:",2*n)
def squares(numbers):
 for n in numbers:
    time.sleep(1)
    print(n," number Square to:  ",n*n)
numbers=[1,2,3,4,5,6]

t1=Thread(target=doubles,args=(numbers,))       # multiple thread execute simultaneously
t2=Thread(target=squares,args=(numbers,))       # multiple thread execute simultaneously
t1.start()
t2.start()
