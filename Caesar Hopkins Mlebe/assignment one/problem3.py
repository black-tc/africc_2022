# Obtain the sentence from the user
sentence = input("Write a sentence of your choice: ")

# Split the words
words = [word for word in sentence.split()]

# Sort the words
words.sort()

# Desplay the sorted words to the user
print("The sorted words are:")
for word in words:
   print(word)
