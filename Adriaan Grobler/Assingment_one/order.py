import string

#take input from user
sentence = input("Welcome to the sorter enter the sentence you would like to order:")

#use for loop to remove any punctuation from the sentence
for char in string.punctuation:
    sentence = sentence.replace(char, "")

#use sort function to alphabetically sort the sentence after spiting it into a list
sorted_list = sorted(sentence.split(" "))

print(sorted_list)