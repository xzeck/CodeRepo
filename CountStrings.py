Words = ["Some", "Random", "Words", "Because", "I", "Have", "To", "Add", "Words", "Into", "This", "List", "I", "Copy", "Pasted", "This", "Lol"]

count = 0 
WordsThatSatisfy = []
for Word in Words:
    if len(Word) > 2 : 
        # Just remove the .upper() if you want to make it case sensitive
        FirstChar = Word[0].upper()
        LastChar = Word[len(Word)-1].upper()
        if FirstChar == LastChar : 
            WordsThatSatisfy.append(Word)
            count = count +1


print("The number of words in the given list that satisfies your condition is : {}".format(count))
print(WordsThatSatisfy)
    
