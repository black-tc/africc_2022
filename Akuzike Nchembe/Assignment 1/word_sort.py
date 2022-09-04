
def word_sort(sentence):
    """
    This function takes a sentence and rearranges the words in alphabetical order
    """
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    sentence = sorted(sentence)
    return sentence

sentence = input("Enter a sentence: ")
sentence = word_sort(sentence)
print(sentence)