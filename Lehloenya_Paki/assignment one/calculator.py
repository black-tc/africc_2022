#!/usr/bin/python3

print("Calculator")

num1 = int(input("Enter your number here: "))
num2 = int(input("Enter your second number here: "))

print("Which arithmetic operator would you like to perform")
print("1. + ")
print("2. - ")
print("3. / ")
print("4. * ")

operator = input("Enter your operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
