# Python program to make a simple calculator

# take inputs
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# choose operation
print("Operation: +, -, *, /")
select = input("Please Select operations: ")

# checks operations and display result
# add(+) two numbers
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

# subtract(-) two numbers
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)

# multiply(*) two numbers
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)

# divide(/) two numbers
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)

else:
    print("Invalid input")