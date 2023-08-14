# index starting from 0
# lenght starting from 1 to n

names = ["Ana","David", "Miska", "Nitol"]
print(names)
length = len(names)
print(length)
print(f"Hi,{names[0]}.") # it will print first name/element from the list
print(f"HI, {names[3]}.") # will print last name/element of the list
print(f"Hi, {names[-1]}.") # reverse indexing, will print last name/element of the list
# print(f"Hi, {names[4]}.") # will generate out of index error
print(f"Hi, {names[length-1]}.") # will print last name/element of the list
