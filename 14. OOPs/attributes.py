# Attributes are just the variables defined inside of a class

# Class attribute: A normal variable created inside a class is a class attribue.

# Instance attribute: A attribute created using an instance like self.name, self.age etc. is known as instance attribute    
class Animal:
    name = "Lion"           #class attribue
    
    def __init__(self, age):
        self.age = age      #instance attribute