profile = {
    'name':'Raju', 'age':27, 'salary':25000.00
}
print(profile)

# used to remove an element from the dictionary
popped = profile.pop("age1",'Not found!')
print(popped)                       # returns the removed element
print(profile)                      # returns the updated dictionary