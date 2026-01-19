#Count vowels in a string
word=input("Enter the string:")
num=0
for ch in word:
    if ch in 'aeiouAEIOU':
        num=num+1
    else:
        continue    
print(num)    