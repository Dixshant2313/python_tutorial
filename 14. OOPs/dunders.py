"""
    Dunder methods are special methods in Python that start and end with double underscores (__) like __init__, __str__, __add__,etc.
    They automatically get called when you perform certain actions on an object.
    They help you for:
        Customize behaviour of your class
        Make your class objects behave like built-in data types like strings, lists, etc.
"""

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"hello {self.name}, how are you"
    
    def __add__(self,other):
        return f"Sum of ages = {self.age + other.age}"
        
obj = Animal("lion",12)
obj2 = Animal("Dolphin", 14)
print(obj + obj2)