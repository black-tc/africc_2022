#Program to sort the words of a sentence alphabetically

print() #linebreak

print("Program to sort words alphabetically")

print() #linebreak

sentence = input("Please write your sentence: ") #asking the user to write the sentence

sentence = sentence.split() #spliting the sentence into individual words to be sorted

sentence.sort(key=str.lower) #sorting the sentence alphabetically (in brackets is to disregard case sensitivity

print() #linebreak

print("The sorted words are: ", sentence) #output the sorted result

