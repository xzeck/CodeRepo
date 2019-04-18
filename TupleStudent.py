
ListOfTuples = []

def AddStudentData():
    n = int(input("\nEnter the number of records you want to enter"))

    for i in range(n): 
        t = (input("Student Name"), input("Roll No"), input("Makrs 1"), input("Marks 2"),
        input("Marks 3"))
        ListOfTuples.append(t)
    pass 

def SearchStudentData():
    NameToSearch = input("\nEnter the name to search")

    for StudentData in ListOfTuples:
        if StudentData[0] == NameToSearch: 
            print("\n")
            for Data in StudentData:
                print(Data)

while True :
    choice = int(input("\nEnter your choice\n1:Add Name\n2:Search Name"))
    if choice is 1 : 
        AddStudentData()
    elif choice is 2 : 
        SearchStudentData()
    else :
        print("Enter valid input")