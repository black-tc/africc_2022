'''
Problem 3: Get a sentence from the user and sort the words in alphabetical order
'''

# Program to sort in alphabetical order the words from a sentence provided by the user
user_input = input("Enter a sentence: ")

# breakdown the string into a list of words
words = [word.lower() for word in user_input.split()]

# sort the list
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)