no=int(input("Enter the No: "))
f= False
if no == 1:
    print(no, "is not a prime number")
elif no > 1:
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    if f:
        print(no, "is not a prime number")
    else:
        print(no, "is a prime number")