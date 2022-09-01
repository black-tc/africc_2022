'''
Problem 1: Simulate the basic calculator function in a simple python program and obtain user 
input to perform the arithmetic operations
'''

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation symbol.")
print("Add\t\t+")
print("Subtract\t-")
print("Multiply\t*")
print("Divide\t\t/")
print("Exit\t\t!")

while True:
    # take user input for both numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # take operation input from the user
    choice = input("Enter operation symbol: ")

    # check if choice is one of the four symbols
    if choice in ('+', '-', '*', '/', '!'):

        if choice == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        elif choice == '!':
            break
    
    else:
        print("Invalid Input")