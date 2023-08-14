# differences set1 = {1, 2, 3, 4} and set2 = {4, 5, 6, 10, 11}
# method and operator(-) can be used
# differences between set1 and set2 would be set1- set2 = {1, 2, 3}

set1 = {'Rick', 'Sam','Jack'}
set2 = {'Jack','Nina','Ash'}
set3 = {'Becky','Popy','Rick'}

# using difference method

# print(set1.difference(set2))
# print(set1.difference(set2, set3))

# using operator
# print(set1 -set2)

# update set
# set1.difference_update(set2)
# print(set1)

# symmetric
#  set1 = {1, 2, 3, 4} and set2 = {4, 5, 6, 10, 11}
# method and operator(^) can be used
# symmetric between set1 and set2 would be set1- set2 = (set1 U set2) - (set1 n set2) = {1, 2, 3, 5, 6, 10, 11}
# however method cannot allowd multiple set but operator allowed

# print(set1.symmetric_difference(set2))
#print(set1.symmetric_difference(set2, set3)) # not allowed will throw an error

# using operator (^)
print(set1 ^ set2)
print(set1 ^ set2 ^ set3)

# update
set2.symmetric_difference_update(set1)
print(set2)
