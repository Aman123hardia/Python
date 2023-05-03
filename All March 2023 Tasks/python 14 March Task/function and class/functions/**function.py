# We can call this function by passing any number of keyword arguments. Internally these
# keyword arguments will be stored inside a dictionary.

def display(**dictionary):
 for k,v in dictionary.items():
  print(k,"=",v)

display(rno=100,name="aman",marks=7,subject="python")    #this function call on keyword argument and it store internally dic