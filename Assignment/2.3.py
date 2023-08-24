class add:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
    
obj1=add(10)
obj2=add(10)
print("Addition: ",obj1+obj2)


        

