DivisibleList = []

for i in range (1, 100):
    if (i % 7 is 0) and (i % 5 is 0):
        DivisibleList.append(i)

for num in DivisibleList : 
    print("\n{}".format(num))