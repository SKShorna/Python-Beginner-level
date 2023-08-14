tuple1 = (5, 3, 6, "Sabira", -90)
tuple2 = (20, )
# tuple3 = (20)
# print(tuple1)
# print(type(tuple1))
# print(type(tuple2))
# print(type(tuple3))

print(tuple1[0])
#tuple1[0] = 6 # it will give an error bcause like list tuple is not allowed to edit, delete, add any element in the tuple, it is immutable
print(f"Tuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print(f"Five times after multiplying one element of the tuple2: {tuple2 * 5}")

#tuple concate nation

tuple5 = (3, 4, 6, "Shorna", 6)
print(f"Tuple5: {tuple5}")
# tuple6 = tuple1 + tuple5
# print(f"After concatening: {tuple6}")
tuple6 = (tuple1, tuple5)
print(f"Tuple6 after concating: {tuple6}")
print(len(tuple6))
print(tuple6[1])
print(tuple5.count(6))
list1 = ["Rayhan, 34, 98, -10"]
print(tuple(list1))
