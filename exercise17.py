# Program to Calculate average height from a list of heights

# # list comprehensions--> important
## can't use in-built sum and len function to solve this
#
# numbers = ['1', '2', '3']
#
# numbers = [int(number) for number in numbers]
# print(numbers)

# height_list = []
# height_all = input("enter the height separated by comma:")
# height_list = height_all.split(",")
# print(height_list)
# add = 0.0
# # list comprehensions
# height_list = [float(height) for height in height_list] # as list input's are string we need to convert it as number
# print(height_list)
#
# for i in height_list:
#     # print(i)
#     add = add + i
#     list_length = 0
#     for item in height_list:
#         list_length += 1
#
#
# # print("The sum of the height is", add)
# else:
#     print(list_length)
#     # avg = add / len(height_list)
#     avg = add / list_length
#     print("The average height:", round(avg, 2))

# height_input = input("Enter your height separated by comma:")
# height_list = height_input.split( )
#
# height_list = [int(height) for height in height_list]
# add = 0.0
#
#
# for i in height_list:
#     add = add + i
#     list_length = 0
#     for x in height_list:
#         list_length += 1
# else:
#     avg = add / list_length
#     print("The average height is:", round(avg))

# Method-2

height = input("Enter your height:")
height_list = height.split()
count = 0
for i in height_list:
    count = count + 1
print(count)

# make list input string to numbers
total = 0.0
for x in range(count):
    height_list[x] = int(height_list[x])
    total = total + height_list[x]
# print("The sum of the total height is:", total)
avg = total / count
print("The average height is:", round(avg))