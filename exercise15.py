#  Program in Python for "Who will pay the bill?"
# Write a program (WAP) that will select a random number from a list of names and the person selected
# will have to pay for everybody's food bill.
# input: Enters everybody's name separated by comma: Jenny, Akash, Payal, Jiya
# output: Jiya will pay the bill (any name)

# # Method-1 using choice
# import random
#
# names_str = input("Enters everybody's name separated by comma: ") # take the input as string with comma
# names_list = names_str.split(',') # make the string took from the user and skip the comma and make it into a list
# # print(names_list)
# print(f"{random.choice(names_list)} will pay the bill.")


# hint: # Convert a comma-separated string to a List in Python

# Use the str.split() method to convert a comma-separated string to a list, e.g. my_list = my_str.split(',').
#
# The str.split() method will split the string on each occurrence of a comma and will return a list containing the results.

# my_str = 'bobby,hadz,com'
#
# my_list = my_str.split(',')
# print(my_list)  # 👉️ ['bobby', 'hadz', 'com']


# Method- 2 not using choice
# import random
#
# names_str = input("Enters everybody's name separated by comma: ")
# names_list = names_str.split(",")
#
# print(names_list)
# names_list[0:4] = [1, 2, 3, 4] # Jenny == 1, Akash == 2, Payal == 3, Jiya == 4
# print(names_list)
# a = random.randint(names_list[0], names_list[3])
# if a == 1:
#     print("Jenny will pay the bill.")
# elif a == 2:
#     print("Akash will pay the bill.")
# elif a == 3:
#     print("Payal will pay the bill.")
# else:
#     print("Jiya will pay the bill.")

# Method-3---important
import random
names_str = input("Enter everybody's name separated by comma:")
names_list = names_str.split(",")
# print(names_list)
# print(len(names_list))
length = len(names_list)
random_choice = random.randint(0, length-1)
print(f"{names_list[random_choice]} will pay the bill.")
