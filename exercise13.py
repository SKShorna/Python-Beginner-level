
# Love Calculator
# True love

# Method-#1
# first_name = input("Enter his/her name:")
# first_name = first_name.lower()
#
# second_name = input("Enter his/her name:")
# second_name = second_name.lower()
# count_true = first_name.count("t") + first_name.count("r") + first_name.count("u") + first_name.count("e") + second_name.count("t") + second_name.count("r") + second_name.count("u") + second_name.count("e")
#
# count_love = first_name.count("l") + first_name.count("o") + first_name.count("v") + first_name.count("e") + second_name.count("l") + second_name.count("o") + second_name.count("v") + second_name.count("e")
#
# love_percent = str(count_true) + str(count_love)
#
# love_percent = int(love_percent)
# if love_percent < 10:
#     print("Sorry!")
#     print(f"Your love percentage {count_true}{count_love} %.")
# elif love_percent > 90:
#     print("Blast!")
#     print(f"Your love percentage {count_true}{count_love} %.")
# elif love_percent > 30 or love_percent < 50:
#     print("Good!")
#     print(f"Your love percentage {count_true}{count_love} %.")
# else:
#     print(f"Your love percentage {count_true}{count_love} %.")
#

# Method- 2

name1 = input("Enter your name:")
name2 = input("Enter His/Her name:")

combine_name = name1 + name2

lower_name = combine_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score} and you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score} and you are alright together.")
else:
    print(f"Your love score is {love_score}")