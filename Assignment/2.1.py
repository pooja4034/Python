age=int(input("Enter Your Age:"))
try:
   if(age<18):
     raise ValueError
except ValueError:
         print("You Are Not Eligible!")
else:
     print("You Are Eligible!")