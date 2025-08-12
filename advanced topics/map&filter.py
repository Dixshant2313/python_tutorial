"""
->  Map is used for applying a function to multiple items.
->  Takes a list(or any sequence)
->  Applies the same function to every item in that list.
->  Gives you back a new list (in Python 3, it gives a map object which you can convert to a list)
"""

# map with lambda function
a = [1,2,3,4,5]
doubled_a = map(lambda x:x**2,a)
print(list(doubled_a))


# map with normal function
def cube(y):
    return y**3

result = map(cube,a)
print(list(result))

# Note: map and filter works better with lambda functions, better to use lambda functions with map and filter

"""
->  Filter as the name suggests is used filter out the stuff.
->  Takes a list(or other sequence).
->  Checks each item using a function (a test).
->  Keeps only the items that pass the test (i.e., returns True)
"""

# filter with lambda function
numbers = [1,2,3,4,5]

evens = filter(lambda x: x % 2 == 0,numbers)
print(list(evens))

# filter with normal function
def odd(y):
    return y % 2 != 0

odds = filter(odd,numbers)
print(list(odds))