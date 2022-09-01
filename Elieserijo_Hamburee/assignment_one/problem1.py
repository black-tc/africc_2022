#!/user/bin/env python

"""
I imported the sys library in order to utilise it to 
to pull in the arguments when the problem1.py module is ran
with an argument
"""
print("- " * 35)
print("This program takes in 2 inputs 'numbers' and an operator and computes the number according to the operator")
print("To view the utilisation manual run python <module> -h")
print("- " * 35)
import sys

"""
Here i defined the calc function that takes in 3 arguments
that the user will be prompted to enter the first argument is the first number
the second argument is the second number and the operation is what the user whats to
with the 2 numbers 
"""
def calc(num1,num2, operation):
    """
    Inside the function I used the if statement together with logical conditions
    in order to check the operation of the user input and calculate the two numbers
    accordingly. At the end an else statement was added to accommodate the case in which
    the user enters an operation that is not accounted for
    """
    if operation == "/": #Checks if the operation is equal to "/"
        # If the operation is equal to "/" it continues to check if the second number is a zero
        if int(num2) == 0:
            #if the second number is a zero a error message will be sent to the user since a number cannot be divided by 0
            print("!!Second number cannot be a zero!!") 
        else:
            #if the second number is not a zero the first number will be divided by the second number and the result
            #will be printed.
            result = int(num1) / int(num2)
            print("Result: " + str(result))
    elif operation == "+":#Checks if the operation is equal to "+"
        result = int(num1) + int(num2) #Adds first and second number
        print("Result: " + str(result)) #Prints the result
    elif operation == "-": #Checks if the operation is equal to "-"
        result = int(num1) - int(num2) #Subtracts the first and second number
        print("Result: " + str(result))#Prints the result
    elif operation == "*" or operation == "x": #Checks if the operation is "*" or "x"
        result = int(num1) * int(num2) #if so multiples the first and second number
        print("Result: " + str(result)) #Prints the result
    else:
    	#If the operation is not equal to anything above this message will be fired
        print("An error occurred please run python <module name> -h for the utilisation manual")
        
#Here we create the banner() function. This function will act as a user manual when the user passes an argument when running the
#this module
def banner():
    print("*" * 50)
    print("For the system to work enter first number and second number as numbers")
    print("For example: ")
    print("Enter the first number: 50")
    print("Enter the second number: 2")
    print("")
    print("For the operation enter either '+', '-', '/' for multiplication use '*' or 'x'")
    print("*" * 50)
    print("")

#The sys.argv is an array which contains the module to be executed and any other arguments specified
if len(sys.argv) == 1: #Checks if the sys.arg array contains only one item
#if the array contains 1 item only the following code is ran
    input1 = input("Enter the first number: ") #Prompt the user to enter first number
    input2 = input("Enter the second number: ") #Prompt the user to enter second number
    operator = input("Please enter the operation: ") #Prompt the user to enter second number
    calc(input1, input2, operator) #Calls the calc function and passes the necessary arguments
elif len(sys.argv) == 2 and sys.argv[1] == "-h":
#The line above checks if the sys.argv array 2 items and if the second item is a "-h" which is passed when the module is ran
#The that is the case the banner function is called
    banner()
    input1 = input("Enter the first number: ")
    input2 = input("Enter the second number: ")
    operator = input("Please enter the operation: ")
    calc(input1, input2, operator)


