class Person: 
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def IsStudent(self):
        return False

class Student(Person): 

    def IsStudent(self):
        return True
    

P = Person("SomeName")
print(P.getName(), P.IsStudent())
S = Student("SomeName")
print(S.getName(), S.IsStudent())
