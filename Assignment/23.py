list1=[1,3,4,5]
print(list1) 
temp = list1[0]
list1[0] = list1[- 1]
list1[- 1] = temp
print(list1)