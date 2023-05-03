
# def wish(name,msg):
#  print("Hello guy my name is ",name," and my message is ",msg)

# wish(name=input("Enter your Name = "),msg=input("Enter your Message = "))


# Here the order of arguments is not important but number of arguments must be matched.

def wish(name,msg):
 print("Hello guy my name is ",name," and my message is ",msg)

wish("aman",msg=input("Enter your Message = "))
# We can use both positional and keyword arguments simultaneously. But first we have to
# take positional arguments and then keyword arguments,otherwise we will get syntaxerror.