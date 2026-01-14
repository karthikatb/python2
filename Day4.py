#Write a Python program to check whether a year is a Leap Year
year=int(input("Enter a year:"))
if year%400==0:
    print("It's a leap year")
elif year%100!=0 and year%4==0:
    print("It's a leap year")    
else:
    print("It's not a leap year")    