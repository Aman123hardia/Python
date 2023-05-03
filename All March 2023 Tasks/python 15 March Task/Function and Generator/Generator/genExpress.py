
# print(table(i*i for x,y in table(range(1,11),int(input("Enter table number")))))
# print(sum(i*i for i in range(10)) )

x = [12, 60, 3]

y = [7, 5, 3]

print(sum(x for x,y in zip(x, y) ))  

