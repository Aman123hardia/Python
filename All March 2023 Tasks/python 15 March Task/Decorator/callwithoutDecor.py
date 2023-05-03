def decor(func):
   def inner(name):
    print(name)
    if name==input("Enter Comparing Name = "):
     print("Hello",name,"Good Morning You are Offline")
    else:
     func(name)
   return inner

def chat(name):
 print("Hello",name,"Good Morning You are Online")

chat=decor(chat)

chat("Durga")
chat("Sunny")