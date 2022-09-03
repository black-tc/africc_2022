# Note that the sortorder priority is Capital letters first (default sort behaviour)
# Example: 
# in: The word of the Lord is a double edged Sword
# out: Lord Sword The a double edged is of the word 
# Author: Evelyn 
# 2 Sept, 2022.

sentence = input("Enter a sentence:\n> ")

# Convert to an array
words = sentence.split()

# Sort
words.sort()

# Print sorted words

for word in words:
    print(word, end=" ")