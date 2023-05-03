# Given two numbers, write a Python code to find the Maximum of these two numbers.
num1=int(input("Enter 1st a number = "))
num2=int(input("Enter 2nd a number = "))
maximum = lambda num1,num2:num1 if num1 > num2 else num2
print("Maximum number is = ",maximum(num1,num2))

