# union, set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 10, 11}
# it will return the set like this {1, 2, 3, 4, 5, 6, 10, 11}
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 10, 11}
#
# # print(set1.union(set2))
# print(set1 | set2) # for this | (union operator both sets operands has to be set otherwise it will throw an error)
#
# # we can add any tuples or list in the union method it will convert it as set and then union
# print(set1.union((100, 200, 300)))

set1 = {'Ram', 'Sam', 'Zain'}
set2 = {'Zain', 'Ash', 'Tom'}
set3 = {'Ryan', 'Pepa'}
# print(set1.union(set2, set3))
# print(set1 | set2 | set3)
# set1.update(set2) # it will update the set 2's elements into the set1
# print(set1)

# inter section set1= {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 10, 11} it will return  the common value which is {4, 5} and opetaor for intersection (&)

# print(set1.intersection(set2))
print(set1 & set2)
set1.intersection_update(set2) # it will update the set1 with the elements that are common in both sets in this case (set1 and set2)
print(set1)