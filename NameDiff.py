s1 = input("Enter First string")
s2 = input("Enter second string")

commonletters = list(set(s1)&set(s2))

print("\ncommon letters : \n")

for letter in commonletters:
    print(letter)

LettersInFirst = list(set(s1).difference(set(s1).intersection(set(s2))))

print("\nLeetters only in first : ")

for letter in LettersInFirst:
    print(letter)

print("\nAll letters of both string :\n{}\n{}".format(s1, s2))

uncommonletters = list(set(s1).difference(set(s2)))

print ("\nuncommon letters : \n")
for letter in uncommonletters:
    print(letter)
