# IF MEMBER ARE NOT ELIGIBEL THAN IT TERMINATE THE PROGRAM ABNORMALLY 
# class TooYoungException(Exception):
#     def __init__(self,arg):
#      self.msg=arg

# class TooOldException(Exception):
#     def __init__(self,arg):
#      self.msg=arg


# n=int(input("How many member in wanted to marige"))
# for count,i in enumerate(range(n)):
#  age=int(input(f"Enter Age person {count+1}:"))
#  if age>60:
#   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
#  elif age<18:
#   raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
#  else:
#    print("You will get match details soon by email!!!")
# print("member are eligible to marry we will contact as soon as possible........")



#HANDLE EXCEPTION OF OUR PROGRAM

class TooYoungException(Exception):
    def __init__(self,arg):
     self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
     self.msg=arg


n=int(input("How many member in wanted to marige"))
for count,i in enumerate(range(n)):
 age=int(input(f"Enter Age person {count+1}:"))
 if age>60:
  try:
   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
  except:
    print("you are too old")
 elif age<18:
    try:
     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
    except:
     print("you are youn wait for .....")
 else:
   print("You will get match details soon by email!!!")
