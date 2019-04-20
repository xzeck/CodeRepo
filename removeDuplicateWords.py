s = input("Enter a string")

new_s = s.split(" ")
RepeatList = []

for words in new_s: 
    if not words in RepeatList : 
        print(words)
        RepeatList.append(words)