
res = 0
try:
    dividend = int(input("Enter Dividend"))
    divisor = int(input("Eenter Divisor"))
    res = dividend / divisor
    
except ZeroDivisionError : 
    print("Can't divide by Zero")
except ValueError: 
    print("Enter a valid input")
finally : 
    print(res)