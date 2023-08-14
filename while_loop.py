# syntax for while loop:
# while condition/expression:
#       statement(s)

# while loop is useful when you don't know how many iteration have to pass, depends on user

# count = 0
#
# while count <= 5:
#     print(count)
#     count += 1
# print("Out of the loop")

# another example

# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print(count)

# using boolean but we need to put a break condition for the while loop
# otherwise it will run forever

# count = 0
#
# while True:
#     print(count)
#     count += 1
#     if count == 3:
#         break
# print("out of loop")

# like for-else while also have while-else block
# if the while block executes successfully without any control break then else block will run

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break
# else:
#     print("in the else block")
# print("Out of the block")
#
# #---------------------------------------
#
# count = 1
# while count < 5: # try it with count < 1 also
#     print(count)
#     count += 1
# else:
#     print("in the else block")
# print("Out of the block")

#  ------------------------------ with list

# numbers = [1, 3, 4, 6]
#
# while numbers:
#     print("Hello! Sabira.")
#     numbers.pop()
# print("Out of the while block")

# Sentinel value- (-1, q or N to quit)

# numbers = int(input("Enter your number (-1 to quit):"))
#
# while numbers != -1:
#     print(numbers)
#     numbers = int(input("Enter your number (-1 to quit):"))
# else:
#     print("In the else block")
# print("Out of the block")

#

numbers = int(input("Enter the number (0 to quit):"))
total = 0
while numbers != 0:
    total += numbers
    numbers = int(input("Enter the number (0 to quit):"))
print("The sum is:", total)
