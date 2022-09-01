#Author: Selakane Khaile
#Date: 08/30/2022

sentence = input("Enter a string: ")  #take user sentence 

words = sentence.split()               #separate the words
words.sort()                #sort the words
for word in words:          #Print the list of words
   print(word)