import nltk 

Data = input("Enter your string")

TokenizedWords = nltk.tokenize.word_tokenize(Data, language='english')
commonWords = nltk.FreqDist(w.lower() for w in TokenizedWords)

FreqeuntWords = commonWords.most_common(3)
print(FreqeuntWords)