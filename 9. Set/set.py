s  = {} # this is not a set, this is an empty dictionary, we need add elements to make it a set

s= {1,2,5,4} # exmaple of set
print(s)

#hash function
b = hash("Hello") # every time this generates a different hash value and that is why sets are unordered
print(b)

c= hash((1,2,344))
print(c)

"""
-> Sets are unordered and elements cannot be accessed using indexing. Each value in set is hashed using a hash function (hash() in python).
-> The hash is used as an index to store the element in memory
-> Since hashing does not maintain order. Sets are unordered
-> Ony immutable (hashable) objects can be stored in a set (e.g. numbers, strings, tuples).

Set cannot be traversed using index values as they are not ordered. It can only be traversed directly over set and will give random values.
"""