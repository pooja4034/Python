class sub:
    def __init__(self,x):
        self.x=x
    def __sub__(self,y):
        return self.x-y.x
    
ob1=sub(10)
ob2=sub(10)
print("substraction: ",ob1-ob2)