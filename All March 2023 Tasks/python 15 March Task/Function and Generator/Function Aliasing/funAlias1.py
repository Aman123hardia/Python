def fun(name): 
	print(f"Hello {name}, welcome to GeeksForGeeks!!!")

cheer = fun
print(f'The id of fun() : {id(fun)}')
print(f'The id of cheer() : {id(cheer)}')
cheer('Geeks')

del cheer
fun('Geeks')


# # get id of list
# a = [1, 2, 3, 4, 5]
# print(id(a))
# b=a
# print(id(b))
# del b
# print(a)
