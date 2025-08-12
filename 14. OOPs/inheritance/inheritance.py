"""
Inheritance allows a class (child class) to inherit the properties and behaviour (attributes and methods) from another class (parent class)

Benefits of using inheritance is:
- Code reusability
- Organized structure
- Easy to maintain and extend
"""

#Syntax is very simpe just like you take parameters in functions here you will take parameters but those parameters will be classes

class Factorymumbai:                    # parent class/ super class
    a = "I am a attribute mentioned inside Factory"
    
    def hello(self):
        print("I am a method mentioned inside Factory")

class Factorypune(Factorymumbai):       # child class/ sub class
    pass

Obj = Factorymumbai()
print(Obj.a)

Obj2 = Factorypune()    # instance of child class
Obj2.hello()

# Now the inherited class has all the powers of parent class that means all the methods, attributes can be accessed by the instance of child class as well

"""
Types of Inheritance

* Single Inheritance
    One child class will inherit from one parent class

* Mutiple Inheritance
    There will be 2 parent classes and only 1 child class will inherit all the attributes and methods of both parents.
"""

