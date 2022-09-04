#!/usr/bin/env python

def calculator():
    num = 1

    while(num==1):          #Validates the menu user input
        choice = int(input("====Calculator====\n1.Sum\n2.Subtraction\n3.Multiplication\n4.Division        \n5.Modulus\n6.Exponentiation\nChoice: "))
        if (choice<1) | (choice>6):
            print("Error! Try again")
        else:
            num=0
            break

    num1 = float(input("Enter the first number: "))     #User input first number
    num2 = float(input("Enter the second number: "))    #User input second number

    if int(choice)==1:                                  #Adition
        print("The result is: ", (num1+num2))
    elif int(choice)==2:                                #Subtraction
        print("The result is: ",(num1-num2))
    elif int(choice)==3:                                #Multiplication
        print("The result is: ",(num1*num2))
    elif int(choice)==4:                                #Division
        print("The result is: ",(num1/num2))
    elif int(choice)==5:                                #Modulus
        print("The result is: ",(num1%num2))
    else:                                               #Exponentiation
        print("The result is: ",(num1**num2))

    if(int(input("Do you wish to continue? \n1.Yes\n2.No\n")))==1:      #Do you wish to continue?
        num = 1
        calculator()
    else:
        print("Bye Hacker :) ")

calculator()