class Calculator :
    def add(self, x, y):
        return x + y
        
    def sub(self, x, y):
        return x - y
         
    def div(self, x, y):
        return x / y
         
    def mul(self, x, y):
        return x * y
        

x = Calculator()

print("\nThe addition of 10 and 20 is {}\n".format(x.add(10,20)))
print("\nThe subtraction of 10 and 20 is {}\n".format(x.sub(10,20)))
print("\nThe multiplication of 10 and 20 is {}\n".format(x.div(10,20)))
print("\nThe division of 10 and 20 is {}\n".format(x.mul(10,20)))