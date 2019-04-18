from os import system # just because I want to do system(cls) not required in the final program

StoreDict = {} 

while True: 
    inputstring = input("Enter the String")
    StoreDict[inputstring] = str(len(inputstring))

    system('cls')

    print(StoreDict)

