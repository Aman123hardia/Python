def simpleGeneratorFun():
    for i in range (1, 4):
        yield i
 
obj =  simpleGeneratorFun()
 
nValue = next(obj)
print(nValue)
nValue = next(obj)
