# used to exit a function and go back the point where it was called from. Fn stops executing after the return statement

def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return(full_name)

name = get_full_name("Shreya","Dixshant Charan")
print(name)

# always use a variable to store the function value while using return statement

"""
-> function naming (function name should be meaningful)
-> function length (user smaller function)
-> avoid global variables
"""