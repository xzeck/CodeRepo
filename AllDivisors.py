num = int(input("Enter your number"))

Range = range(1, num+1//2)

for i in Range: 
    if num % i is 0 :
        print("\n{}".format(i))

