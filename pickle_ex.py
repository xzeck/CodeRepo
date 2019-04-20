import pickle 
import os 

path = os.path.dirname(os.path.abspath(__file__))

class Student: 
    def __init__(self,id, name, division, department):
        self.id = id 
        self.name = name
        self.division = division 
        self.department = department
    
    def display(self):
        print("\nID : {}\nName : {}\nDivision : {}\nDepartment : {}".format(self.id, self.name, self.division, self.department))

n = int(input("Enter the number of student data you want to enter"))
Db = open(path + '\\DbFile.txt', 'ab')
for i in range(n):
    sid = int(input("Enter student ID\n"))
    sName = input("Enter name of student\n")
    sDiv = input("Enter division\n")
    sDep = input("Enter department\n")
    Obj = Student(sid, sName, sDiv, sDep)
    pickle.dump(Obj, Db)

Db.close()

Dept = input("Enter department to search")
Db = open(path + '\\DbFile.txt', 'rb')

while True: 
    try : 
        Obj = pickle.load(Db)
        if Dept == Obj.department :
            Obj.display()
    except EOFError: 
        print("End of file")
        break

    