limit=int(input("enter the limit:"))
number=int(input("enter the number:"))
big=number
second_big=big
small=number
second_small=small
while(limit>1):
    number = int(input("enter the number:"))
    if number>big:
        second_big=big
        big=number
    elif number>second_big:
        second_big=big
    if number<small:
        second_small=small
        small=number
    elif number<second_small:
         second_small=small
    limit=limit-1
print("largest=",big)
print("second_largest",second_big)
print("smallest",small)
print("second_smallest",second_small)



