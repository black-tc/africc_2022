user = input("Enter the string: ")

words = sorted(user.split(), key=str.lower)

for word in words:
   print(word)