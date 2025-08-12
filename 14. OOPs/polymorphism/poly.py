"""
Polymorphism is a core concept in OOp. The word means 'many forms' and in programming, it allows the same interface or method name to behave differently depending on the object or context.
"""

class Animal:
    def __init__(self, name):   #constructor
        self.name = name
    
    def show(self):     #instance function
        print(f"Hello your name is {self.name}")
        
class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def show(self):
        print(f"Hello your name is {self.name} and age is {self.age}")
  
animal1 = Animal("lion")
person1 = Human ("shreya",20)

animal1.show()
person1.show()


'''
Method overriding :- If a child class inherits a parent class and they have a method whose name is same, then the object will be calling the method of child class (overriding the method of parent class)

class Animal:
    def show(self):
        print("Hello 1")

class Human:
    def show(self):
        print("Hello 2")
        
obj = Human()
obj.show()    -> the method show of Human class (child) overrides the method of Animal class (parent) printing "Hello 2"
'''

'''
Duck Typing :- Python follows the philosophy-
                "If it walks like a duck and quacks like a duck, it must be a duck."

class Animal:
    def show(self):
        print("Show is showing)
        
class Human:
    def show(self):
        print("I am also showing")
        
obj1 = Animal()
Obj2 = Human() 

obj1.show()
obj2.show()

Both the methods will run and give their respective output as they are created within separate classes and objects.
'''