'''
- If we talk about function we can ask the user parameters, but in class we cannot have parameters for that we use constructor.
- A constructor is a method that runs automatically when we call a class and this constructor function will target obj location
'''


class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def show(self):
        print(f"Your object details are: {self.material},{self.zips},{self.pockets}")
    
reebok = Factory("leather",3,2) 
campus = Factory("nylon",3,3)

# self is used to capture the location of the object

reebok.show() # this function will print the object details for reebok as self holds the location value of reebok