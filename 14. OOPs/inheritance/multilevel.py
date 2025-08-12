class Factory:          #parent class
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
        
class BhopalFactory(Factory):       #child class
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
        
class PuneFactory(BhopalFactory):   #grandchild class
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        
obj = PuneFactory()
# PuneFactory will inherit all the four attributes (Factory -> BhopalFactory -> PuneFactory)

# We also have one more type of inheritance i.e Hierarchial inheritance which simply means that 2 child classes will have 1 parent class.