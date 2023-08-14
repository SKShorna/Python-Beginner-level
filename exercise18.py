# Program to find maximum numbers from a list of numbers (Coding exercise-15)
# have to take input from the user
# cannot use in-built max() function

numbers = input("Enter the numbers:")
number_list = numbers.split()
print(number_list)

count = 0
for i in number_list:
    count += 1

for number in range(count):
    number_list[number] = float(number_list[number])
    maximum = number_list[number]
    if number_list[number] > maximum:
        maximum = number_list[number]
else:
    print("The maximum number is", round(maximum))
