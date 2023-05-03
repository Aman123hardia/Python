from threading import *
import time
def cube(numbers):
 for n in numbers:
  time.sleep(1)
  print("cube:",n*n*n)

def squares(numbers):
 for n in numbers:
  time.sleep(1)
  print("Square:",n*n)
  
numbers=[1,2,3,4,5,6]

cube(numbers)
squares(numbers)
