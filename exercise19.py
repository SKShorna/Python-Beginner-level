# Calculate sum of even numbers from 1 to 100 (including 1 and 100)
# Method-1

numbers = range(1, 101)
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number
print("The sum of the numbers is:", total)

# Method-2
# for number in range(2, 101, 2):
#     total += number
# print("The sum of the numbers is:", total)
