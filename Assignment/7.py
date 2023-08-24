no = int(input("Enter a number: "))
sum = 0
temp = no
while temp > 0:
   dig = temp % 10
   sum += dig ** 3
   temp //= 10
if no == sum:
   print(no,"is an Armstrong number")
else:
   print(no,"is not an Armstrong number")