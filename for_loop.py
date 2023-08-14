# for loop in python is traversing any sequence
# sequence means collection of elements such as strings, lists, dictionary
# syntax: for variable_name in sequence

# nam_str = 'Sabira'
# for i in nam_str:
#     print(i)
#
# names = ['Rick', 'Sabira','Nina','Zack']
# for name in names:
#     print(name)
#     if name == 'Sabira':
#         print("Hey, It's me.")

# finding the square of the lists
numbers = [2, 3, 5, 10, -2]
list1 = []
for i in numbers:
    square = i ** 2
    list1.append(square)
print(list1)
