import os 

path = os.path.dirname(os.path.abspath(__file__))

s = input("Enter data to append")

File = open(path + '\\FileAppend.txt', 'r')
FileData = File.readlines()

print("\nData before appending : \n{}".format(FileData))

File.close()
File = open(path + "\\FileAppend.txt", 'a+')
File.writelines(s)
File = open(path + "\\FileAppend.txt", 'r')
FileData = File.readlines()
print("\nData after appending : \n{}".format(FileData))




