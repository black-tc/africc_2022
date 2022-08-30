"""
The function strSort() takes in a string then converts it to lowercase since I noticed that when sorting alphabetically, uppercase letters are considered first despite their position in the alphabet. The string is then coberted into a list of words using the split() method and the list sorted using the sort() method. -Emmanuel Kenedi, 2022
"""

def strSort(strng):
	strng = strng.casefold()
	strng = strng.split()
	strng.sort()
	y = ""
	for x in strng:
		y += " "+x
	print("\nSorted sentence: \n")
	print(y)
		
print("Word Sorter by Emmanuel Kenedi\n\n")
strng = input("Enter sentence to sort: ")
strSort(strng)