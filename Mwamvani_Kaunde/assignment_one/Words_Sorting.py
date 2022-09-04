# A program that get a sentence from the user and sort the words in alphabetical order
Sentence = input("Type your sentence below: \n")  # getting input from the user

Words = Sentence.split()  # breakdown the sentence into a list of words

Words.sort()  # sorting the words

# displaying sorted words
print("See the sorted words below: \n--------------------------")
for Word in Words:
    print(Word)