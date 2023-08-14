# range syntax : range(start, stop, stepsize)
# formula: start(i), stop(j) and stepsize(k)
# so i, i_k, i+2k, i+3k.... and j-1

# a = range(5)
# print(a[0])
# print(a[1])
# for i in a:
#     print(i)
# print("Another range example:")
# for x in range(2, 10, 2):
#     print(x)

# print("Another range example with negative step-size:")
#
# for z in range(10, 0, -1):
#     print(z)

# Quiz: Have to add numbers from 1 to 100 and print the sum
total = 0
for i in range (1, 101):
    total = total + i
print("The sum is:", total)