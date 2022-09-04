# Author: Rueben Elias
# Date: 31 August 2022
# Project Description: Alphabetical Sort

# Function to sort the words in alphabetical order
def F(S):
	W = S.split(" ")
	for i in range(len(W)):
		W[i] = W[i].lower()
	W.sort()

	# return the sorted words
	return ' '.join(W)

# Driver code
S = input("Enter your sentence: ")
print(F(S))
