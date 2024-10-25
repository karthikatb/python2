'''
author karthika tb
date 25/10/2024
discription Write a Python program to convert temperature values back and
forth between Celsius and Fahrenheit. The user should be able to
input a temperature in Celsius or Fahrenheit, and the program should convert
it to the other unit using the formula:
'''
temperature=int(input("enter temperature"))
scale=(input("Is this in (C)elsius or (F)ahrenheit?"))
if scale=="c":
    f = (9/5*temperature) + 32
    print(temperature, "is celcius",f,"fahrenheit")
else:
    c=5/9*(temperature-32)
    print(temperature,"is faherenheit",c,"celsius")
