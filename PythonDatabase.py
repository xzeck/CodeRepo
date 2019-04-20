import sqlite3

conn = sqlite3.connect("Student.db")
c = conn.cursor()

def AddData(name, roll, avg):
    c.execute('INSERT INTO Record VALUES (?,?,?)', (int(roll), str(name), float(avg)))

def DeleteData(roll):
    c.execute('DELETE FROM Record WHERE Roll = (?)', roll)
    pass

def SearchData(roll):

    pass


while True: 
    choice = int(input(("\nEnter your choice \n1:Add data\n2:Delete Data\n3: Search Data")))
    
    if choice is 1: 
        name = input("Enter the name")
        roll = int(input("Enter the roll no"))
        avg =  float(input("Enter the avg data"))
        AddData(name, roll, avg)

    elif choice is 2 :
        roll = int(input("Enter the roll no to delete"))
        DeleteData(roll)
    elif choice is 3 :
        roll = int(input("Enter the roll no to search"))
        SearchData(roll)
    else :
        print("Please Enter a valid input")
