a = {1,2,3,4,5}
b = {4,5,6,7,8}

union_set = a.union(b)
print(union_set)        #returns a new set with all the elements from both sets
# union (A|B)

intersection_set = a.intersection(b)
print(intersection_set) #returns only the common elements from both sets
# Intersection (A&B)

difference_set = a.difference(b)
print(difference_set)   #returns only the elements present in set A (excluding the common elements)
# Difference (A-B)

symmetric_diff = a.symmetric_difference(b)
print(symmetric_diff)   #returns all elements except the common elements
# Symmetric difference = (A^B)

#compund operation can be performed on the sets
