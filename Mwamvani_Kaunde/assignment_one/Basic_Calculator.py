# Program to simulate the basic calculator functions

# Addition function
def add(m, k):
    return m + k

# Subtraction function
def subtract(m, k):
    return m - k

# Multiplication function
def multiply(m, k):
    return m * k

# Division function
def divide(m, k):
    return m / k

# Prompts user to select the function
print("Select one from the available four operations: ")
print("----------------------------------------------")
print("1.Add \n2.Subtract \n3.Multiply \n4.Divide")
print("----------------------------------------------")

while True:
    # taking input from the user
    choice = input("Please enter your choice (1 to 4): ")

    # checking if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        FirstNumber = float(input("Enter first number: "))  # operand1
        SecondNumber = float(input("Enter second number: "))  # operand2

        if choice == '1':
            print( FirstNumber, "+", SecondNumber, "=", add( FirstNumber, SecondNumber))

        elif choice == '2':
            print( FirstNumber, "-", SecondNumber, "=", subtract( FirstNumber, SecondNumber))

        elif choice == '3':
            print( FirstNumber, "*", SecondNumber, "=", multiply( FirstNumber, SecondNumber))

        elif choice == '4':
            print( FirstNumber, "/", SecondNumber, "=", divide( FirstNumber, SecondNumber))

        # checking if user wants another calculation
        # break the while loop if answer is n
        Another_Calculation = input("\nDo you want to do another calculation?"
                                    "\nPress n to cancel or any letter to continue: ")
        if Another_Calculation == "n":
            break

    else:
        print("Invalid Input")