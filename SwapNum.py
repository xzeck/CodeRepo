n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))

if n1 < 0 :
    print("\n{} is negative".format(n1))
elif n1 > 0 : 
    print("\n{} is positive".format(n1))
else : 
    print("\nThe first number is zero")


print("\nBefore swapping : n1 = {}, n2 ={}".format(n1,n2))

# Swapping
t = n1 
n1 = n2 
n2 = t

print("\nAfter swapping : n1 = {}, n2 = {}".format(n1,n2))



