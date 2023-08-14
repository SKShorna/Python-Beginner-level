height = int(input("What is your height?"))
bill = 0

if height < 3:
    print("Can ride")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 1
        print("Ticket price is $1.")
    elif age < 18:
        bill = 2
        print("Ticket price is $2.")
    else:
        bill = 5
        print("Ticket price is $5.")
    want_photo = input("Do you want photo? Type 'Y/N': ")
    if want_photo == 'Y' or want_photo == 'y':
        bill = bill + 50
    print(f"Your bill is {bill}.")
else:
    print("Can't ride.")
print("Thank you... Enjoy the ride!")