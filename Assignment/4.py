year = int(input('Enter year : '))
 
if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "Is Leap Year")
else :
    print(year, "Not Leap Year")