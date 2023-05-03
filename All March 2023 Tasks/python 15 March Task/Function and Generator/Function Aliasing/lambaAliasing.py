
def hello():
    for i in range(5):
        print(i)
 
s=lambda a:a()   # function aliasing as a argument
s(hello)