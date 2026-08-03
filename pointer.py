'''
num1=11
print("num1=",num1)
num2=num1
print("num2=",num2)
print("\nnum1 points to:",id(num1))
print("num2 points to:",id(num2))
num2=23
print("---------------------------------")
print("num1=",num1)
print("num2=",num2)
print("\n num1 points to:",id(num1))
print("num2 points to:",id(num2))
'''
dict1={"value":1}
dict2=dict1
print("Dict1 points:",id(dict1))
print("Dict2 points:",id(dict2))
dict2["value"]=2