Number = int(input("Enter your Number"))

sum = 0

for i in range(1, Number):
    if Number % i is 0:
        sum = sum + i

if sum is Number: 
    print("The number is a perfect number")
else :
    print("The number is not a perfect number")