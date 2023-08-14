# disjoint set- it is those sets where no elements are in common
# set1 = {1, 2, 3, 4, 5} and set2 = {4, 10, 7, 8, -10} this is not disjoint set because we 4 in common in both sets
# method is isdisjoint() but no operator

set1 = {'Rick', 'Sam','Jack'}
# set2 = {'Jack', 'Nina'}
set2 = {'Jacky', 'Nina'}
# print(set1.isdisjoint(set2)) # will return false because there is a common (Jack)

# subset, we can say set1 is subset of set2 if set2 contains every element of set1 or
# set1 is subset of set2 if every elements of set1 is in set2
# method issubset() and operator also (<=)
set2 = {'Jacky', 'Nina','Rick', 'Sam','Jack'}
# print(set1.issubset(set2))
# print(set1 <= set2)

# Superset - reverse of subset
# set1 is superset of set2 if set1 contains every element sof set2
# method issuperset() and operator (>=)
set1 = {'Jacky', 'Nina','Rick', 'Sam','Jack', 'Popy','Glory'}
set2 = {'Jacky', 'Nina','Rick', 'Sam','Jack'}
print(set1.issuperset(set2))
print(set1 >= set2)


# to remove element from the set clear() method
# to remove elements including set use del
# set2.clear()
# print(set2)

#  delete entire set

del set2
print(set2)


