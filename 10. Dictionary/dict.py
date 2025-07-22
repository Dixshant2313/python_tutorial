"""
Dictionary is a data type in python which is used to store data in key and value pairs separated by comma.

-> These were unordered before python version 3.7, now they are ordered
-> Mutable (keys cannot be changed however the values can be changed)
-> Keys must be unique whereas the values can be a duplicate
-> Dictionary follows insertion order (there are no indexes, however it takes place on keys)
-> They are heterogenous.
"""

d = {10:100,20:100,30:300,40:400} #basic example of dictionary
print(d[10])                      #values can be accessed by using keys (as there is no indexing in dict)

# We can perform CRUD operations on values. However, keys cannot be changed after creation.
d[10] = 1000
print(d)

#traversing a dictionary
for i in d:
    print(i)     # will provide the keys
    print(d[i])  # will provide the values
