list1 = [11, 12, 13, 14, 15]  
list2 = [12, 13, 11, 15, 14]  
list3 = [37, 15, 11, 80, 14] 
list1.sort()
list2.sort() 
list3.sort()
if list1 == list2:  
    print("The list1 and list2 are the same")  
else:  
    print("The list1 and list3 are not the same")  
      
if list1 == list3:  
    print("The list1 and list2 are not the same")  
else:  
    print("The list1 and list2 are not the same")