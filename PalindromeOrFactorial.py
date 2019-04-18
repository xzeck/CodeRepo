import sys

def Palindrome(Number) :
    temp = Number 

    Reverse = 0
    while Number > 0 :
        Reminder = Number % 10
        Reverse = (Reverse*10) + Reminder 
        Number = Number // 10
    
    if temp == Reverse :
        return True 
    else :
        return False

def Factorial(Number):
    sum = 1
    if Number == 0 or Number == 1:
        return 1  

    for i in range(1, Number+1) :
        sum = sum * i

    return sum


choice = '1'

while choice !=  'q' : 
    number = int(input("Enter the number"))
    choice = input("\nEnter your choice : \n1 - Palindrom\n2- Factorial")

    if choice == '1':
        IsPalindrome = Palindrome(number)
        if IsPalindrome == True:
            print("{} is palindrome".format(number))
        else :
            print("{} is not palindrome".format(number))
    
    elif choice == '2':
        Fact = Factorial(number)
        print("Factorial of {} is {}".format(number, Fact))

    elif choice == 'q':
        sys.exit(0) 
    else :
        print("Wrong Choice")

