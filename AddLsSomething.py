Userinpt = input("Enter string\n")

CheckLs = Userinpt[:2].upper()

if CheckLs == 'LS':
    print(Userinpt)
else :
    print ('ls' + Userinpt)
