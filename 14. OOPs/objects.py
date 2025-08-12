'''
- Objects are the instance of the class
- It is very easy to create objects you just have to call the class inside a variable and that becomes an object
- The object has all the powers of a class 
'''

class Fruit():
    name = "Apple"
    
f = Fruit()     # creating an object
print(f.name)   # accessing the attribute a with the help of object 


# Another example
class Animal():
    name = "Lion"
    
    def sound(self):
        print("Roar!")
    
obj = Animal()  # we have created an object of class Animal and all things inside can be accessed by the object
print(obj.name) # accessing the attribute name
obj.sound()     # accessing the method sound