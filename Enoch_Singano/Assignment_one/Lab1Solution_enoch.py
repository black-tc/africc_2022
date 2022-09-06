import os
import sys
import time
import datetime
import calendar

"""This is the first Python Practice Lab1 Assignment
   THis program has been developed by Enoch Singano
   Author: Enoch Singano"""

# Main Menu for a user to select a function
def menu():
    print("")
    print("\033[31m" + "\033[1m" + "	   PYTHON PRACTICE LAB1 - ENOCH SINGANO AFRICC " + "\033[0m")
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   0	|Information, Instructions and Disclaimers	|")
    print("|   1	|A Simple Calculator		                |")
    print("|   2	|Display Calendar	                        |")
    print("|   3	|Print Words in Alphabetic Order			|")
    print("|   99	|Exit 			                			|")
    print("=========================================================")

    try:
        a = input("Type your option: ")

        if a == "0":
            info_page()
        elif a == "1":
            calculator()
        elif a == "2":
            calendar_function()
        elif a == "3":
            alphabetic_order()
        elif a == "99":
            os.exit(0)
        else:
            print(" input a possible option.")
            time.sleep(1)


    except:
        print("Please input a possible option.")
        time.sleep(1)

# Calculator Function
def calculator():
    # Simple Calculator Simulator in Python

    # ADDITION FUNCTION
    def add(a, b):
        return a + b

    # SUBTRACTION FUNCTION
    def sub(a, b):
        return a - b

    # MULTIPLICATION FUNCTION
    def multi(a, b):
        return a * b

    # DIVISION FUNCTION
    def division(a, b):
        return a / b

    print("This is a Calculator \n Please Select Operation:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVISION")

    while True:
        # take input from the user
        choice = input("Please enter your choice:")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

            # check if user wants anothr calculation

            next_calculation = input("Do you want to do next calculation? (yes/no):")

            if next_calculation == "no":
                print('Thank you for using my calculator \n Enoch')
                break

# Calendar Function
def calendar_function():
    # This function prints out the calendar month inputted by the user

    y = int(input('Enter the year:'))
    x = int(input('Enter the month'))

    print(calendar.month(y, x))

# Function to sort words in alphabetical order
def alphabetic_order():

    my_str = input('This program sorts words in Alphabetic order \n Enter a string (words): \n')


    words = my_str.split()

    # sort the list
    words.sort()

    # display the sorted words
    for word in words:
        print(word)

def info_page():
    print("This program has been developed by Enoch Singano. \n Choose an option you  want from the Menu as Displayed\n"
          "The 1st option is a Calculator"
          "2nd Option is displays the calendar month desired by the user.\n"
          "The 3rd Option sorts words entered by the user in Alphabetic Order.\n"
          "")

menu()
