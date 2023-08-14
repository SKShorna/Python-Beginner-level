# Pizz Order Program
# Small Pizza = 100 or $1
# Medium Pizza = 200 or $ 2
# Large Pizza = 300 or $3

# Pepperoni for small Pizza = 30
# Pepperoni for medium or large Pizza = 50
# Extra cheese for any size Pizza = 20


pizza_size = input("Enter your Pizza size(S/M/L or s/m/l):")
bill = 0

if pizza_size == 'S' or pizza_size == 's':
    bill += 100
    print("Small Pizza Price is 100 taka.")
    # want_pepperoni = input("Do you want to add pepperoni? Type 'Y/N': ")
    # if want_pepperoni == 'Y' or want_pepperoni == 'y':
    #     pepperoni = 30
    #     bill = bill + pepperoni
elif pizza_size == 'M' or pizza_size == 'm':
    bill += 200
    print("Medium Pizza price is 200 taka.")
    # want_pepperoni = input("Do you want to add pepperoni? Type 'Y/N': ")
    # if want_pepperoni == 'Y' or want_pepperoni == 'y':
    #     pepperoni = 50
    #     bill = bill + pepperoni
else:
    bill += 300
    print("Large Pizza price is 300 taka.")
    # want_pepperoni = input("Do you want to add pepperoni? Type 'Y/N': ")
    # if want_pepperoni == 'Y' or want_pepperoni == 'y':
    #     pepperoni = 50
    #     bill = bill + pepperoni

want_pepperoni = input("Do you want to add pepperoni? Type 'Y/N': ")
if want_pepperoni == 'Y' or want_pepperoni == 'y':
    if pizza_size == 'S' or pizza_size == 's':
        bill += 30
    else:
        bill += 50

want_extra_cheese = input("Do you want extra cheese? Type 'Y/N': ")
if want_extra_cheese == 'Y' or want_extra_cheese == 'y':
    bill += 20
print(f"Your total bill is {bill}")


