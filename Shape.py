from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimeter(self):
        pass
    pass 

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def getArea(self):
        return 3.1415 * (self.r**2)
    
    def getPerimeter(self):
        return 2 * 3.1415 * self.r
    

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l 
        self.b = b

    def getArea(self):
        return self.l * self.b
    
    def getPerimeter(self):
        return 2 * self.l * self.b
    pass 


C = Circle(10)
R = Rectangle(10,20)

print("For Circle The Area is : {}. The Perimeter is : {}\n".format(C.getArea(), C.getPerimeter()))

print("For Rectangle The Area is : {}. The Perimeter is : {}\n".format(R.getArea(), R.getPerimeter()))