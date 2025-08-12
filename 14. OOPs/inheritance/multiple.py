"""
* Mutiple Inheritance
    There will be 2 parent classes and only 1 child class will inherit all the attributes and methods of both parents.
    The constructor function will be inherited of the first class that has been inherited. This is MRO(Method Resolution Order) followed by pyhthon.
"""

class Animal:
    def __init__(self,name):
        pass
    
class Human:
    def __init__(self,name,age):
        pass
    
class Robot(Animal,Human):  #multiple inheritance
    name = "Chitti"
    
obj = Robot()
# In above example the child class "Robot" will inherit only name from the parent class "Animal" as per the MRO
# class Animal is passed first in Robot but if we reverse the order i.e "class Robot(Human, Animal)" -> name and age both will be 
# inherited as the MRO changes