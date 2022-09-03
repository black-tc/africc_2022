# To perform an operation just type it e.g. 'add'
# You can also type operation number as presented on the menu
# e.g. 1 for Add.
# Input is case insesitive
# Author: Evelyn
# 2 Sept, 2022

def operation(operand):
    op = operand.lower()
    a = eval(input("Enter first number:\n> "))
    b =  eval(input("Enter second number:\n> "))

    if op == "add" or op == "1":
        return a+b
    elif op== "subtract" or op == "2":
        return a-b
    elif op == "multiply" or op == "3":
        return a*b
    elif op == "divide" or op == "4":
        return a/b
    else:
        print("Invalid operand!")
        exit()

def main():
    op = input("Operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\nSelect\n> ")
    result = operation(op)
    print("The result is ", result)

main()