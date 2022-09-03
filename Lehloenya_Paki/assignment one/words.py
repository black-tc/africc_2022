#!/usr/bin/python3

import sys


sen = input("Enter your sentence: ")

words = sen.split()
words.sort()

for word in words:
    sys.stdout.write(word + " ")
    sys.stdout.flush()


