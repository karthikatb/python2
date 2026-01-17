#Count digits in a number
num=int(input("Enter a number:"))
i=0
while num>0:
    i+=1
    num=num//10
    
print(i)    
    