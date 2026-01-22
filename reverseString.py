#Reverse a string
str=input("Enter the string:")
print(str[: :-1])

rev=" "    
for ch in str:
    rev=ch+rev
print(rev)        