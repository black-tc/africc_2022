"""
@author: Junior Moremong
description: Program that sorts words in a sentence in alphabetical order
"""
#read sentence from user
sentence = input("What's on your mind?:")

#store string into list
wordy = sentence.split(" ")

#sort list
wordy.sort(key=str.lower)

#join list back to string
str1 = ' '.join(wordy)
print(str1)