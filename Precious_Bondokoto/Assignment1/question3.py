my_sentence = input("Enter the desired sentence: ")

words = [word.lower() for word in my_sentence.split()]


words.sort()

print("The words in alphabetical order are:")
for word in words:
   print(word)
