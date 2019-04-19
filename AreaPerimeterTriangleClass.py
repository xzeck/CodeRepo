import math

class Triangle : 
    def __init__(self, s1, s2, s3): 
        self.s1 = s1
        self.s2 = s2 
        self.s3 = s3 
    
    def getArea(self, p):
        return math.sqrt(p*((p-s1)*(p-s2)*(p-s3)))

    
    def getPerimeter(self):
        return s1 + s2 + s3

s1 = int(input("Enter the length of side 1\n"))
s2 = int(input("Enter the length of side 2\n"))
s3 = int(input("Enter the length of side 3\n"))

CallObj = Triangle(s1, s2, s3)

print("Perimeter is : {}".format(CallObj.getPerimeter()))
p = CallObj.getPerimeter()
print("Area is : {}".format(CallObj.getArea(p/2)))
