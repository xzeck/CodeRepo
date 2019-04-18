s1 = int(input("Enter side 1\n"))
s2 = int(input("Enter side 2\n"))
s3 = int(input("Enter side 3\n"))


if s1 == s2 == s3 : 
    print("Equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3 :
    print ("Isoceles Triangle")
else : 
    print("Scalene Triangle")