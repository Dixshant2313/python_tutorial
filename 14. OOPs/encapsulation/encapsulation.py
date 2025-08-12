'''
class Factory:
    a = "Delhi"
    
    def show(self):
        print("Delhi factory")
        
obj = Factory()  # this creates an instance (object) of class Factory and it can access all things inside it
print(obj.a)

obj.a = "Pune"
print(obj.a)    # this will change the attribute value

# Now suppose I want to modify the access of things inside my class, there comes the role of encapsulation
'''

"""
Encapsulation means putting data (variables) and code (functions) together in one place - inside a class.
It also means hiding the internal details of how things work, and only showing what is needed.
-> It keeps data safe from being changed by mistake.
-> It makes your code clean and easy to use.
-> It gives control over what others can access or change.
"""

#Access modifier in python
"""
Access modifiers means how we give access of our attributes and methods to the object or inherited classes. There are 3 types of access modifiers, let see them one by one:

1. Public Attributes and Methods:
   Till now every attribute and methods we have created are public means the inherited classes and objects can access them no matter what.
"""

class Car:
    name = "ferrari"
    
    def show(self):
        print("Ferrari 458 Italia ")
        
class Mclaren(Car):
    def show2(self):
        print(super().name) # this super function is able to access attribute from parent class
        
obj = Mclaren()
obj.show2()


"""
2. Protected Attributes and Methods:
    Python protected members are created using a single underscore but it still can be accessed from outside the class so you might wonder what is the point of using them.
    Python doesn't enforce protected access like other languages (e.g. Java or C++). But it uses a naming convention to tell developers. (This means it same as public attributes and methods).
"""

class Factory:
    _a = "pune" #protected attribute
    
    def _show(self):
        print("Pune Factory")
        
class Bhopal(Factory):
    def show2(self):
        print(super()._a)
        
obj = Bhopal()
obj.show2()

"""
3. Private Attributes and Methods:
    It cannot be accessed from outside the class - only from inside the class where it is defined.
    In python, we use two underscores(__) before the name to make it private.
"""

class Animal:
    __name = "lion"
    
    def __show(self):
        print("I am a lion")
        
#   def show(self):
#       print(Animal.__name)  Only can be accessed inside the class where it is created
        
lion = Animal()
print(lion.__name)
lion.__show()

# another example
class Demo:
    def __init__(self):
        self.name = "Public Member"     #Public
        self._age = 21                  #Protected
        self.__salary = 42000           #Private
        
    def show(self):
        print("Inside the class:")
        print("Public:", self.name)
        print("Protected:", self._age)
        print("Private:", self.__salary)