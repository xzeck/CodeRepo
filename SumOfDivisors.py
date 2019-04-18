Number = int(input("Enter the number"))

sum = 0 

for i in range(1, Number) : 
    if Number % i == 0 :
        sum = sum + i

print("The sum of the divisors of the {} is {}".format(Number, sum))