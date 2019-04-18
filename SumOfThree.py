n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))

t1 = n1 - n2 
t2 = n2 - n3 

res = n1 + n2 + n3

if t1 == 0 or t2 == 0:
    print("The sum is : {}".format(res * 3))
else :
    print("The sum is : {}".format(res))

