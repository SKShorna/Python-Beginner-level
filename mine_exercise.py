# # Exercise 5:
# Write a program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards). Print "Palindrome" if it is a palindrome, and "Not a palindrome" otherwise.

# Solution: Method-1: using slicing

# input_str = input("Enter your string:")
# # print(input_str)
#
# # reverse_str = input_str[::-1] # or
# reverse_str = input_str[len(input_str)::-1]
#
# if len(input_str) > 1:
#     if reverse_str == input_str:
#         print("Palindrome.")
#     else:
#         print("Not a palindrome.")
# else:
#     print("Invalid input.")

# Solution-1: not using slicing

input_str = input("Enter your string:")
# print(input_str)
is_palindrome = True
length = len(input_str)
# print(length)
for i in range(length // 2):
    if input_str[i] != input_str[length - i - 1]:
        is_palindrome = False
        break


if is_palindrome:
    print("Palindrome.")
else:
    print("Not a palindrome.")



