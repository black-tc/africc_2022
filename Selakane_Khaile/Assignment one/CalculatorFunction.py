#Author: Selakane Khaile
#Date: 08/30/2022

def multilpication (x,y): #multiplication
    return x * y

def subtraction (x,y):    #subtraction
    return x - y

def addition (x,y):       #addition
    return x + y

def devision (x,y):      #devision
    return x / y

def exponent (x,y):
    return x ** y

#User Menu
print ("\nChoose From Below Avalabe operations")
print ("1.To Multiply")
print ("2.To Subtract")
print ("3.To Add")
print ("4.To Devid")
print ("5.Exponetiate \n")

while True:
    selection =input ("Enter selection: \n")
    if selection in ('1','2','3','4','5'):

        firtNumber = int(input("Enter first number: "))
        
        seconNumber = int(input("Enter second number: "))

        if selection =='1':
            print ("Answer of ",firtNumber," * ",seconNumber," = ",multilpication(firtNumber,seconNumber))
            print ("Bye!")
            break
        elif selection =='2':
            print ("Answer of ",firtNumber," - ",seconNumber," = ",subtraction(firtNumber,seconNumber))
            print ("Bye!")
            break
        elif selection =='3':
            print ("Answer of ",firtNumber," + ",seconNumber," = ",addition(firtNumber,seconNumber))
            print ("Bye!")
            break
        elif selection=='4':
            print ("Answer of ",firtNumber," / ",seconNumber," = ",devision(firtNumber,seconNumber))
            print ("Bye!")
            break
        elif selection =='5':
            print ("Answer of ",firtNumber," ^ ",seconNumber," = ",exponent(firtNumber,seconNumber))
            print ("Bye!")
            break
    else:
        print ("Please select from give range.")