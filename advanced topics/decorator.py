"""
->  A decorator is just a function that modifies another function without changing its actual code.
->  Imagine you have a cake (your function). A decorator is like puttong icing on the cake. It doesn't change the cake itself,
    but makes it better, prettier or adds some new flavor!
->  For creating a decorator, you first have to create a decorator functions and then inside that we will create a wrapper.

class Animal:
    @property   #decorator
    def show(self):
        print("Hello how are you")
        
obj = Animal()
obj.show()
obj.show    # because of property decorator this can work without calling the show function
"""

def decorate(func):     #decorator function accepting the original function
    def wrapper(a,b):   #wrapper function taking the arguments similar to original function
        print("The addition to the numbers are ")
        func(a,b)
        print("Thankyou I hope you liked it ")
    return wrapper      

@decorate   #decorator
def addition(a,b):  #original function
    print(f"Sum of the numbers = {a+b}")

addition(12,67)