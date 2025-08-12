"""
For making the decorator with Arguments it is tough, for this we will move towards 'args', 'kwargs'.
-> They are special keywords in python used in function definitions to accept a flexible number of arguments.
-> Now you always don't have to use Args and Kwargs the main thing is *,** you can use any name in front of them.
-> And the 'args' becomes a tuple and 'kwargs' becomes a dictionary.
-> The use case is great
    You don't need to know how many inputs you'll get.
    Helps in building flexible functions, decorators, APIs and more.
"""

def addition(*args):    # args - stores all the arguments passed in the function in a tuple
    sum = 0
    for i in args:
        sum += i
    
    print(sum)     
    
addition(12,12,23,56)


def information(**kwargs):
    print("Your infromation is\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
    
information(Name = "Shreya", Age = 20, DOB = "10/05/2005", Gender = "F")

#decorator using args and kwargs

def decorate(func):
    def wrapper(*args,**kwargs):
        print("The product of your two numbers is ")
        func(*args,**kwargs)
        print("Thankyou")
    return wrapper

@decorate
def product(a,b):
    print(f"Product = {a*b}")
    
product(5,4)