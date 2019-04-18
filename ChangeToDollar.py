Input = input("\nEnter your string")

FirstChar = Input[0]
NewString = Input[1:].replace(FirstChar, "$")

print(NewString)