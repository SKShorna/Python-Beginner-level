# welcome to the Password Generator!
# How many letters would you like in your password? 4
# How many symbols would you like? 5
# How many numbers would you liKe? 2

# 1st task-Easy one-> password should not be shuffled
# 2nd task-Hard one-> password should be shuffled

# Method-1 - I solved-very basic- using choices instead of choice
import random
# print("Welcome to the Password Generator!")
#
# # get input from the user for number of letters
# pass_letter = int(input("How many letters would you like in your password?"))
#
# all_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#               'v', 'w', 'x', 'y', 'z', 'A', 'B',
#               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
#               'X', 'Y', 'Z']
#
# # chose the letters randomly regarding the user input size
# pass_let_only = random.choices(all_letter, k=pass_letter)
#
# # print the output as a list with individual list items according to the random choice
# print(pass_let_only)
#
# # make the list to convert as string
# fix_let = ""
# for letter in pass_let_only:
#     fix_let += str(letter) + ""
#
# # print the letters as users input size as string such as ['a', 'B', 'c', 'd'] would be "aBcd"
# print(fix_let)
# # print(type(fix_let))
#
# # ask user for symbols like previous (letter case)
# pass_sym = int(input("How many symbols would you like?"))
#
# all_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{','}', '?', '~', '_', '-', '=']
# pass_sym_only = random.choices(all_symbol, k=pass_sym)
# fix_sym = ""
# for sym in pass_sym_only:
#     fix_sym += str(sym) + ""
# print(fix_sym)
#
# pass_num = int(input("How many numbers would you liKe?"))
# fix_dig = ""
# for i in range(pass_num):
#     dig = (random.randint(0, 9))
#     fix_dig += str(dig) + ""
# print(fix_dig)
#
# # concatenate the entire password in order (letter+ symbol+ number)
# your_pass = fix_let + fix_sym + fix_dig
# print("Your password without shuffle:", your_pass)
# print(type(your_pass))
#
# # Process for password print not in order
# # shuffling the password
# # this is just one solution but there could be many good one
#
# # an empty list,
# l = []
#
# # then insert the ordered password into the new empty list
# for i in your_pass:
#     l.append(i)
# print(l)
# # shuffle the newly created list
# random.shuffle(l)
# # it will print a shuffled list
# print(l)
#
# # time to convert the shuffled lists items into strings
# # print the shuffled password
# your_pass = ""
# for j in l:
#     your_pass += str(j) + ""
# print(f"Your password with shuffle:{your_pass}")

# ######################################Method-2- Jenny's solution (better than mine)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B',
              'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
              'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{','}', '?', '~', '_', '-', '=']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

n_letters = int(input("How many letters would you like in your password?"))
n_symbols = int(input("How many symbols would you like in your password?"))
n_digits = int(input("How many digits would you like in your password?"))

password_list = []

for i in range(1, n_letters+1):
    char = random.choice(letters)
    password_list += char         # password = password + char
print(password_list)

for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password_list += char
print(password_list)

for i in range(1, n_digits):
    char = random.choice(digits)
    password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char
print(password)





