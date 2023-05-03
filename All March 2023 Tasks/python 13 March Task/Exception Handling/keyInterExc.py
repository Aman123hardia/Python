try:
  name  = input('Enter the name of the user ')
except EOFError:
    print('Hello user it is EOF exception, please enter something and run me again')
except KeyboardInterrupt:                                             #this is keyInterput Exceptions handle
    print('Hello user you have pressed ctrl-c button.')
else:
    print('Hello user there is some format error')