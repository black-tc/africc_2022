#!/user/bin/env python

import sys 

print("- " * 35)
print("This program takes in a sentence and sorts it in alphabetical order")
print("- " * 35)
#The banner above prints what the module does
userString = input("Please enter a sentence: ") #Prompts the user to enter a sentence
#The split method will split the userString into a list and stores it into the variable array of word
arrayOfWords = userString.split() 

#arrayOfWords.sort() 
#Each word in the arrayOfWords list will be made lowercase to avoid and mistakes and stores it into the words variable
words = [word.lower() for word in arrayOfWords]
#The sort function sorts the words list alphabetically
words.sort()
#Finally the words are joined into a single string to form a sentence
alpha_order = " ".join(words)
print(alpha_order)

