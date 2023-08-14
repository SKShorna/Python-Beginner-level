# break-out from the loop (or closest inner loop)
# break - if want to exit from the block of the loop
# continue - if want to skip some part of block of the loop
# pass -  do nothing-- > for future work


count = 1

while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("Hi")
print("OUt from the loop")

# with nested for loop

# list1 = ["Hi", "Hello", "welcome"]
# names = ["Nina", "Rick", "Jack"]
#
# for item in list1:
#     for name in names:
#         print(item, name)
#         if item == "Hello" and name == "Rick":
#             break
#     print("Out from the inner loop")
# print("Out from the outer loop")

# while loop with continue
# count = 1
# while count <=10:
#     print(count)
#     count += 1
#     if count == 7:
#         continue
#     print("Hi")
# print("Out from the loop")

# for loop with break

# for i in range(1, 11):
#     print(i)
#     if i == 7:
#         continue
#     print("Hi")
# print("Out from the loop")


# while loop with pass

# count = 1
# while count <=10:
#     print(count)
#     count += 1
#     if count == 7:
#         pass
#     print("Hi")
# print("Out from the loop")


# for loop with pass

# count = 1
# while count <=10:
#     print(count)
#     count += 1
#     if count == 7:
#         pass
#     print("Hi")
# print("Out from the loop")

# another example for pass

# for i in range(5):
#     pass
#
# # pass with function
#
# def fun1():
#     pass