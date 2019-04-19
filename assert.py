
# Note : Run the two parts of the code independently, since when assertion is executed
# it stops the flow of execution and the User defined exception is not executed. 


# assertion example
x = 10 
y = 0 

assert y != 0, "Cannot divide by 0"
print(x/y)


# User Defined exception
class LessThanZeroException(Exception):
    pass

try : 
    if y <= 0 :
        raise LessThanZeroException

except LessThanZeroException: 
    print("Value Less than Zero")