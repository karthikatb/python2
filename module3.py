list1=[45,34,67,89,444]
list2=[1,12,33,22,45,5]
combined_list=list1+list2
print("first list:",list1)
print("second list:",list2)
print("combined list:",combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
    even_list.sort()
    odd_list.sort()
print("even list",even_list)
print("odd list",odd_list)
list3=even_list+odd_list
print(list3)


