"""
@author: Junior Moremong
description: Program to perform basic arithmetic operations on input read from the keyboard.
"""
# function that takes in operands and the signs of the operator, then returns result.
def calculate(x,sign,y):
    if sign == '+':
        return x + y
    elif sign == '-':
        return x - y
    elif sign == '/':
        return x/y
    elif sign == '*':
        return x * y

x = float(input("Enter first operand:"))
sign = input("Enter arithmetic operator:")
y = float(input("Enter second operand:"))   
result = calculate(x,sign,y)
print("%.2f %c %.2f = %.2f" %(x,sign,y,result))