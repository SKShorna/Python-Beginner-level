# check whether a given year is leap year or not
# exercise_

year = int(input("Enter the year: "))

if year > 0:
    if year % 400 == 0 or year%400 ==0 and year%100 !=0:
        print("This is a leap year")
    else:
        print("Not a leap year.")
else:
    print("Invalid input")
