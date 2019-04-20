from functools import reduce 

def mapfunc():
    str1 = input("Enter numbers").split(" ")
    str1 = [int(i) for i in str1]
    str2 = [list(map(lambda x:x**2, str1))]
    print(str2)
    pass 

def listcompfunc():
    str1 = input("Enter weight").split(" ")
    str1 = [int(i) for i in str1]
    str2 = ["normal" if i < 80 else "overweight" for i in str1]
    print(str2)
    pass 

def filterfunc():
    str1 = input("Enter Age").split()
    str1 = [int(i) for i in str1]
    str2 = list(filter(lambda x:x<=18, str1))
    print(str2)
    pass 

def reducefunc():
    str1 = input("Enter numbers").split()
    str1 = [int(i) for i in str1]
    str2 = reduce(lambda x,y:x if x>y else y, str1)
    print(str2)
    pass


# mapfunc()
# listcompfunc()
# filterfunc()
reducefunc()
