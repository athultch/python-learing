year = int(input("enter a year "))

if(year % 400 ==0 ) and (year %100 ==0):
    print(year ,"it is a leap year")
elif (year % 4 == 0 ) and (year % 100 != 0):
    print(year ,"it is a leap year")
else :
    print(year ,"not a leap year")
    