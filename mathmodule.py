'''
author:karthika tb
date:18-10-2024
Python program that uses functions from the math module to perform
the following operations on a number provided by the user:
'''
import math
number=int(input("enter a number:"))
square_root=math.sqrt(number)
print("square root of",number,":",square_root)
factorial=math.factorial(number)
print("factorial of",number,":",factorial)
power=math.pow(number,2)
print(number,"raised to power2:",power)