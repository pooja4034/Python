a = 100
b = 1000
for no in range(a, b + 1):
   order = len(str(no))
   sum = 0
   temp = no
   while temp > 0:
       dig = temp % 10
       sum += dig ** order
       temp //= 10
   if no == sum:
       print(no)