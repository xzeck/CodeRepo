StudentList = ["Student1", "Student2", "Student3", "Student4", "Student5", "Student6"]

choice = ''


def addStudent():
    n = int(input("\nEnter the number of students you want to add"))

    for i in range(0, n): 
        name = input("\nEnter student's name")
        StudentList.append(name)
    pass 

def search():
    NameToSearch = input("\nEnter the name to search for")
    for i in range(0, len(StudentList)):
        if StudentList[i] == NameToSearch:
            return i
    
    return -1

while choice != 'q':
    choice = input("\nEnter your choice :\n1:Add Student\n2:Sort\n3:Search")

    if choice is '1' :
        addStudent()

    elif choice is '2' :
        StudentList.sort()
        for student in StudentList:
            print(student)

    elif choice is '3' :
        index = search()
        if index is -1:
            print("\nThe name is not in the record")
        else : 
            print("\nThe student record is at : {}".format(index))
    else :
        print("Enter valid number")