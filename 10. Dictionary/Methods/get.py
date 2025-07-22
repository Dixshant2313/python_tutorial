profile = {
    'name':'Raju', 'age':27, 'salary':25000.00
}
print(profile)

# get() method -> used to retreive the value of a key present in the dictionary
# syntax -> dictionary_name.get(key,"message to be displayed if the key does not exist")

age = profile.get('age',"No macth found!")
print(age)