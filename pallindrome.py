#Write a Python program to reverse a number
num=int(input("Enter the number to reverse:"))
rev=0
temp=num
while num>0:
    n=num%10
    rev=rev*10+n
    num=num//10
print("Reversed number",rev)    
if temp==rev:
    print("The number is pallindrome")
else:
    print("It's not a pallindrome")    