
# Find out how many days, weeks and months we have left, if we live untill 90 years old.
# 1 year = 365, 1 year = 52 weeks and 1 year = 12 months

# input = your current age
# output = You have a days, b weeks and c months left.

age = int(input("Enter your age: "))

years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")