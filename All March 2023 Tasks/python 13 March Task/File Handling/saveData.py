
f = open('data.txt', 'w')
line1=input("Enter first line data ")
line2=input("Enter Second line data")
line3=input("Enter third line data")

lines=[line1,'\n', line2,'\n', line3,'\n']
f.writelines(lines)
f.close()