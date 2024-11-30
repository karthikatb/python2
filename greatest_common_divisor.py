'''
def maximum(num1,num2,num3):
    number=[num1,num2,num3]
    number.sort()
    return number[2]
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number: "))
custom=maximum(num1,num2,num3)
print("the largest number is",custom)
'''
#Write a Python function to sum all the numbers in a list.
'''
def add(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
list=[]
element=int(input("enter the elements:"))

for i in range(element):
    num=int(input("enter the number:"))
    list.append(num)
print(list)
add(list)
'''
'''
def product(list):
    multi=1
    for i in list:
        multi=multi*i
    print(multi)
list=[]
element=int(input("enter the elements:"))

for i in range(element):
    num=int(input("enter the number:"))
    list.append(num)
print(list)
product(list)
'''
'''
def reverse(str):
    return str[-1::-1]
custom=input("enter the numbers: ")
print(reverse(custom))
'''
