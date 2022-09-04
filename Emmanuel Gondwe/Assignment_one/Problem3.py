userInput = str(input ("Enter a Sentence that you would like to be sorted in reverse order:\n"))

userInput= userInput.split()[::-1]

wordsBuffer = []

for i in userInput:
    
    wordsBuffer.append(i)

print(" ".join(wordsBuffer))

