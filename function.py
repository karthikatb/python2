def is_even(num):
    if(num%2==0):
        return True
    else:
        return False

number=int(input("Enter the number"))
print(is_even(number))


def is_leap(year):
    
    if (year%4==0 and year%100!=0)or ( year%400==0):
        return True
    else:
        return False
        
year = int(input("Enter the year"))
print(is_leap(year))
