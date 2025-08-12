"""
- Abstraction does not exist in python but we can achieve it using a library.
- Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecesarry details.
- It is used to define a common interface for different subclasses.

Abstract Classes and Methods
* These are classes that contains one or more abstract methods
* A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.
"""

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Square(abstract):
    def __init__(self,side):
        self.side = side
        
    def perimeter(self):
        print("Created")

    def area(self):
        print("Created Area")

class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius
        
    def perimeter(self):
        print("Created")

    def area(self):
        print("Created Area")
        
obj = Circle(7)
obj2 = Square(12)