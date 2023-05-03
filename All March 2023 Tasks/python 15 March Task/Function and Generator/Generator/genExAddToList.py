genEx = (a for a in range(5))

def genFun():
    yield 5
    yield 6
b = genFun()
lst1 = []
lst2 = []

for i in genEx:         
    lst1.append(i) #data add to list

for i in b:
    lst2.append(i) #data add to list
print(lst1, lst2)


# print(gen()[:2] )    # generators don't support indexing or slicing
# print( [5,6] + gen()) # generators can't be added to lists
