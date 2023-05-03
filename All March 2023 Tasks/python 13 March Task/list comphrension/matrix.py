matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

row =[[row[i] for row in matrix] for i in range(4)]
print(row[0])
print(row[0][0])

# for i in row:
#     for j in i:
#         print(j, end='  ') #print all  row wise
#     print()
    
    

for i in range(3):
    for j in row:
         print(j[i], end='   ')
    print()