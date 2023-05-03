
#unpack list
colors = ['red', 'blue', 'green']
red, blue,green = colors
print(red,blue,green)


#unpack tuple
colors =(1,2,3)
red, blue,green = colors
print(red,blue,green)


#unpack dic
my_dict = {'A': 300, 'B': 150, 'C': 500, 'D': 850, 'E': 400}

my_list = list(my_dict.values())

print(my_list)
print(type(my_list))