
# Program to swap two numbers
# temp variable is helping to swapping the other variables (a and b)

a = input("Enter value of a = " )
b = input("Enter value of b = ")

print("Before swapping, " + "Value of a = " + a + " and " + "Value of b = " + b)
temp = a
a = b
b = temp
print("After swapping:")
print("Value of a = " + a)
print("Value of b = " + b)