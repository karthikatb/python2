str1=input("Enter the first string:").lower().replace(" ","")
str2=input("Enter the second string:").lower().replace(" ","")
if sorted(str1)==sorted(str2):
    print("its's a anagram")
else:
    print("it's not a anagram")    