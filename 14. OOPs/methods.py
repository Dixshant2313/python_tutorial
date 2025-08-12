'''
Methods are the functions defined inside the class

Instance Method:- An instance method works with instance(obj) of the class. This method can access and modify instance attributes.

Class Method:- This method works with the class itself, it will not target the instance (object). We have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.

Static Method:- This method doesn't access class or instance directly it also uses a decorator @staticmethod. It just acts like a regular function placed inside a class
'''

class Animal:
    name = "lion"   #class attribute
    
    def __init__(self, age):
        self.age = age  #instance attribute
        
    def show(self): #instance method
        print(f"Son of a bitch, you are {self.age} years old")
        
    @classmethod
    def hello(cls): #class method
        print("Motherfucker")
        
    @staticmethod
    def static():   #static method
        print("How are you")
        
obj = Animal(12)    #creaing an instance
obj.show()          #calling the instance method
obj.hello()         #calling class method (cls captures the location of class)
obj.static()        #calling static method 
