# Function to sort the words 
# in ascending order 

 
sentence = input("Enter a sentence: ")
# Splitting the Sentence into words 

words = sentence.split() 

# Sorting the words 
words.sort()  

sentence = " ".join(words)
print(sentence)