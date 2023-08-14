# a = 5
# b = 5
# c = '5'
# # a = 6
# print(id(a))
# print(id(b))
# print(id(c))
#
# print(a is b)
# print(a is c)
# print(a is not c)

a = 5
print(id(a))

a = 8

print(id(a))
print(a is a)



# The expression a is a checks if a and a reference the same object.
# Since a is reassigned to reference the 8 object,
# the expression a is a evaluates to True because a and a both reference the same object 8.