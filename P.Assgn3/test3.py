year = input("year")

if (year % 400 == 0) and (year % 100 == 0):
    print(" is a century leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print(" is a plain leap year")


else:
    print(" is not a leap year")