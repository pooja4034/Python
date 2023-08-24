n=int(input("Enter No:"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("The factorial is : ", end=" ")
print(fact)
a=0
b=1
print("Fibonacci Series:", a, b,end=" ")
for i in range(2, n):
    c = a + b
    a = b
    b = c
    print(c,end=" ")

