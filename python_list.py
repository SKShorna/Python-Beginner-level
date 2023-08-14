# Note: also can check official python method documentation

numbers = [10, 0, 80, -7, 56]
print(numbers)
# names = ['Sabira', 'Rayhan', 'Mukul', 'Shorna']
# print(names)
# mix_list = [10, 'Sabira', 23, 'Rayhan']
# print(mix_list)

print(len(numbers))

# # indexing/slicing
# print(numbers[0:5]) # print entire list [index : length of the list]
# print(numbers[:])   # print the entire list
# print(numbers[0:])  # print the entire list
# print(numbers[:5]) # print the entire list
#
# # print the particular range of the list
# print(numbers[1:5])
# print(numbers[2:4])
#
# # print skip by numbers
# print(numbers[1:5:2])
#
# # reverse printing
# # print(numbers.reverse()) # it will return None, so the reverse first then print
# numbers.reverse()
# print(numbers)

# # sort the list
# # print(numbers.sort()) # it will return None, 1st sort the list then print
# numbers.sort()
# print(numbers)

# # min , max
# print(min(numbers))
# print(max(numbers))

# # append one at a time in the list
# numbers.append(45)  # it will append at the end of the list
# print(numbers)

# # insert numbers with or without indexwise
# numbers.insert(1, 46) # it will insert the number at the index i position of the list and shift rest of the numbers in the list
# print(numbers)

# add more than one numbers in the list
numbers.extend([47, 48, 49, 50])
print(numbers)

# replace existing numbers with index
numbers[1:4] = [34, 35, 36]
print(numbers)

# pop out numbers

print(numbers.pop(2))
print(numbers)

# list to string


