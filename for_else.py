# for else, not like if-else
# syntax: for variable_name in sequence:
#                 statement(s)
#         else:
#                 statement(s)
# else statement will only work when  for loop works successfully
# no break inside the for loop will work else successfully

# numbers = [2, 3, 5, -4, 0, 10]
#
# for i in numbers:
#     print(i)
# else:
#     print("for loop Successfully Completed and we are in else block now!")

# using break inside the forloop then else will not work

# numbers = [2, 3, 5, -4, 0, 10]
# numbers = (2, 3, 5, -4, 0, 10)
# for i in numbers:
#     print(i)
#     if i == 0:
#         print(f"for loop does not work and else block will not work after having {0}")
#         break
# else:
#     print("for loop Successfully Completed and we are in else block now!")
# print("We are out of for-else loop now")

numbers = (2, 56, 34, 3, 5, -1)
for i in numbers:
    print(i)
    if i % 6 == 0:
        print(i)
        break
    # else:
    #     print("There is no number divisible by 6 in this sequence.")
else:
    print("There is no number divisible by 6 in this sequence.")
print("We are out of for-else loop now")