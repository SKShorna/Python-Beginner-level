# set items are not ordered like list and tuples
# indexing cannot possible in set
# in set any immutable item like tuples can be added but list cannot be because list can be changed

set1 = {10, True, 22, -10, 'Sabira', 25} # every time it will print different order of elements
# True and 1 consider as same so it will print either True or 1, no duplicate elements
print(set1)
print(type(set1))
# set1[2] = 23 # It will give an error because like list indexing is not possible in sets
# print(set1)
set2 = {}
print(type(set2)) # it will print type as dict

# to declare an empty set we have to use set function as follows
set3 = set()
print(type(set3))

# to add elements in the list
set1.add(89)
print(f"After adding number into the set1:{set1}")

# to remove element from the list can use remove or discard
set1.remove(89)
print(f"After removing 89 from the set1:{set1}")
# discard will not throw any exception if the number is not in the set

set1.discard(68)
print(f"After using discard and number 68 that is not in the list: {set1}")

# pop to remove element however it will return the element that is popped

pop_element  = set1.pop() # it will remove any random element from the set
print(f"After using pop: {set1}")
print(f"The element that has been popped:{pop_element}")

# we can add any non changable item such as tuples not list in the set
set1.add((23, 24, 25))
print(f"After adding immutable item in the set1: {set1}")


