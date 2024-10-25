'''
author karthika tb
date 25-10-2024
description
 Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.

Sample Input:
'''
number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the third number"))
if number1>number2 and number1>number3:
    print(" the largest number is:",number1)
elif number2>number3:
    print("the largest number ",number2)
else:
    print("the largest number is:",number3)