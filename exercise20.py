# FizzBuzz Job interview Question

# divisible by 3 --> Fizz
# divisiblw by 5--> Buzz
# divisible by both 3 & 5 --> FizzBuzz

for i in range(1, 16):
    if i % 3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
