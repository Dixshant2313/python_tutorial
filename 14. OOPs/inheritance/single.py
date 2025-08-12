"""
Constructors in inheritance
    Let say you have created a parent class with a constructor function inside it and then this class is inherited by another class, then the constructor function of parent class will work for the child class as well.
"""

class Animal:   #parent class / super class
    def __init__(self, name):
        self.name = name        #instance attribute
        
    def show(self):             #instance method
        print(f"Hello your name is {self.name}")
        
class Human(Animal):    #child class / sub class
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
    
    def show(self):             #instance method
        print(f"Hello your name is {self.name},{self.age}")

animal1 = Animal("lion")
person1 = Human("Hitler", 23)

animal1.show()
person1.show()

"""
Now lets say you need a new parameter in your child class you have to create a constructor function for your child class, but the parameters that can be initialized in the parent class will be initialized using the super() function. Super function will target the parent class.
"""