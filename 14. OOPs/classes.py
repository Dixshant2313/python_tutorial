# Classes is like a blueprint or template for creating objects.

# Syntax of class :- a class is created with a basic keyword class and a name in front of it.
class Factory:
    brand = "Toyota"
    
'''
-> Creating a class is super simple now lets see what is inside class. There are 2 types of things inside class
  * Attributes:- Variables defined inside the class
  * Methods   :- Functions defined inside a class
'''

class Number:
    a = 12                      # attribute
    
    def hello(self):            # method
        print("How are you")  
        
    print("Hello I am getting initialzed") #this is initialzed with the first time a class is created whether class is called/not
    
Factory()  #class calling

'''
A class is initialised only one time when we first run the program, and for accessing the attributes and methods we have to first access the class and then the attributes and methods.
'''
# print(a) -> if you try to access (a), this will give an error

print(Number().a) #accessing a with class
Number().hello()  #accessing hello function with class


# Another example
class Animal:
    type = "Cat"    #attribute
    
    def sound(self):
        print("Meow!")
        
#Directly accessing attribute and method using class
print(Animal().type)
Animal().sound()

'''
Self is a way for instance methods to refer to the object they are being called on. It gives access to the object attributes and other methods.

We'll get to it later, just know that the program won't run without the "self" keyword
'''