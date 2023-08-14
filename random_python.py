import random

# Random module is built in and has a list number of functions such as

# # rnadint(a, b) --> a <= X <= b-- it will return a random number including a and b number
# a = random.randint(1, 3)
# print(a)

# # randrange(a, b) --> a <= X < b-- it will return a random number including a and not b number
#
# a = random.randrange(1, 3)
# print(a)

# # random--> it will return a float number ranging from 0.0 <= x < 1.0
#
# a = random.random()
# print(a)

# # uniform--> it will return a float number for particular range
# a = random.uniform(1, 3)
# print(a)

# # choice--> it will return a number from a list
#
l = [1, 3, 5, 8, 3]
a = random.choices(l)
print(a)


################################################

l = ['1', '3', '5', '8', '3']
a = random.choices(l, k=2)
print(a)
m = ""
for i in a:
    m += str(i) +""
print(m)





###################
# suffle --> shuffle the list
# l = [1, 3, 5, 8, 3]
# random.shuffle(l)
# print(l)

# pass_letter = int(input("How many letters would you like in your password?"))
# # print(type(pass_letter))
# all_letter = 'abBcC'
# password_letter_only = random.choices(all_letter, k=pass_letter)
# print(password_letter_only)
# print(type(password_letter_only))