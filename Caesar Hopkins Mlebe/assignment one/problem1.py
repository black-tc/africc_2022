print("My Simple calculator")
#get input from the user
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

#get operation choice from the user
operation = input("Choose operation: \n1. Add\n2. Multiply \n3. Divide \n4. Subtract \n\n")

#function to operate on the input by the user
def operate(x):
    match int(x):
        case 1:
            return int(number1) + int(number2)
        case 2:
            return int(number1) * int(number2)
        case 3:
            return int(number1) / int(number2)
        case 4:
            return int(number1) - int(number2)
        case default:
            return "wrong input"
#calling the operate function
sum = operate(operation)

#loop to ensure that user inputs right operation
while sum == "wrong input":
    operation = input("\nINVALID OPERATION \nPlease choose valid operation: \n1. Add\n2. Multiply \n3. Divide \n4. Subtract \n\n")
    sum = operate(operation)

#display answer based on switch condition
match int(operation):
    case 1:
        print("{0} add {1} is {2}".format(number1, number2, sum)) 
    case 2:
        print("{0} multipy {1} is {2}".format(number1, number2, sum))
    case 3:
        print("{0} divide {1} is {2}".format(number1, number2, sum))
    case 4:
        print("{0} subtract {1} is {2}".format(number1, number2, sum))
    case default:
        print("Sorry!, Couldn't operate")
        