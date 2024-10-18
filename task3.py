'''
author:karthika tb
date:18-10-2024
Python program that demonstrates the usage of arithmetic,
comparison, and logical operators. Perform a few operations and print the results.
'''
number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
print("sum=",number1+number2,"division=",number1/number2)
print("Is a greater than b?:",number1>number2)
print("Are a and b equal?:",number1==number2)
print("Logical AND:",number1>0 and number2>0)
print("Logical AND:",number1<0 and number2>0)
print("Logical OR:",number1>0 or number2<0)