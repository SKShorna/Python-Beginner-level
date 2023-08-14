
# round(number, no of digits)

print(round(7))  # will return integer 7
print(type(7))

print(round(7, 0)) # will return integer 7

print(round(7.66666, 2)) # will return integer 7.67
print(type(7.66666))

print(round(7.66666)) # will return integer 8 because greater than 5

print(round(7.5)) # will return nearest even number which is 8
print(round(6.5)) # will return nearest even number which is 6

print(round(674, 0)) # will return 674

print(round(674, 2)) # will return 674

print(round(674, -2)) # will return 700 because mulitple of 200 hundred and closest number

print(round(674, -3)) # closest number and mulitple of (10)^3 which is 1000

print(round(674, -4)) #it will return zero because there is no number that is closest mulitple of 10000

print(round(-8/3))
print(round(-8/3, 2))
print(round(-1.5))  # will return  nearest even number -2
print(round(-2.5)) # will return nearest even number  -2
