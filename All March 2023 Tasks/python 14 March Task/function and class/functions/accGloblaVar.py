# If global variable and local variable having the same name then we can access
# global variable inside a function as follows
# accessing global variable when same name as local 
a=10         #global variable  
def f1():
 a=777 #local variable
 print(a)
 print(globals()['a'])
 
f1()