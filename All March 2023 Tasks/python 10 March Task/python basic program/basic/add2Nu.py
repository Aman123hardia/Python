# Python program to add two numbers
num1=int(input("Enter 1st a number = "))
num2=int(input("Enter 2nd a number = "))
sum = num1+num2
print("sum of ",num1," and ",num2,"  is = ",sum)

#using list compherison find max
x=[num1 if num1>num2 else num2]
print("maximum number is:",x)


#find max by sort method
x=[num1,num2]
x.sort()
print(x[-1])
