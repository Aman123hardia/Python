# a, b = 0, 1
# while a < 50:
#     pass
#     a, b = b, a+b
#     print(a,b)
# b=0
# aman=[]
# while b<5 :
#  aman.append(int(input("enter a number")))
#  b+=1
# print(aman)
pairs = [(4, 'one'), (2, 'two'), (3, 'three'), (1, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs[1][0])