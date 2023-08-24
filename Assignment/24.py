list1=[17,67,4,3,8,90]
print(list1) 
temp = list1[0]
list1[0] = list1[2]
list1[2] = temp
print(list1)