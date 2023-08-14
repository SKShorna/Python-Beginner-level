
# Lec_04: variables in python

name = input("What is your name? ")
# print(name)
length = len(name)
print(length)

# a = 1
b = "Rayhan"

# print(a + b) # it will generate an TypeError: because different data type
# (integer and string cannot be concat like this way )

print(name + " " + b)  # it will work because by default input function return variable as string
