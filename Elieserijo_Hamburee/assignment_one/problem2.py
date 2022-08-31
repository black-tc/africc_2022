#!/user/bin/env python

"""
I imported the sys library in order to utilise it to 
to pull in the arguments when the problem1.py module is ran
with an argument. The calendar library will be used to print the calendar
based on the arguments passed
"""
import calendar
import sys

print("- " * 35)
print("This program takes in a month and year as and input and outputs the calender of that year and month")
print("To view the utilisation manual run python <module> -h")
print("- " * 35)

#Here we create the printCalender function that takes in the month and year arguments
def printCalendar(month, yy):
    if month == "January" or month == "Jan" : #Checks if the month is equal to January or Jan
        print(calendar.month(yy,1))#If that is the case it prints the calendar for January in the specified year
    elif month == "February" or month == "Feb":#Checks if the month is equal to February or Feb
        print(calendar.month(yy,2))#If that is the case it prints the calendar for February in the specified year
    elif month == "March" or month == "Mar":#Checks if the month is equal to March or Mar
        print(calendar.month(yy,3))#If that is the case it prints the calendar for Marchin the specified year
    elif month == "April" or month == "Apr":#Checks if the month is equal to April or Apr
        print(calendar.month(yy,4))#If that is the case it prints the calendar for April in the specified year
    elif month == "May": #Checks if the month is equal to May
        print(calendar.month(yy,5))#If that is the case it prints the calendar for May in the specified year
    elif month == "June" or month == "Jun": #Checks if the month is equal to June or Jun
        print(calendar.month(yy,6))#If that is the case it prints the calendar for June in the specified year
    elif month == "July" or month == "Jul": #Checks if the month is equal to July or Jul
        print(calendar.month(yy,7))#If that is the case it prints the calendar for July in the specified year
    elif month == "August" or month == "Aug":#Checks if the month is equal to August or Aug
        print(calendar.month(yy,8))#If that is the case it prints the calendar for August in the specified year
    elif month == "September" or month == "Sept":#Checks if the month is equal to September or Sept
        print(calendar.month(yy,9))#If that is the case it prints the calendar for September in the specified year
    elif month == "October" or month == "Oct":#Checks if the month is equal to October or Oct
        print(calendar.month(yy,10))#If that is the case it prints the calendar for October in the specified year
    elif month == "November" or month == "Nov":#Checks if the month is equal to November or Nov
        print(calendar.month(yy,11))#If that is the case it prints the calendar for November in the specified year
    elif month == "December" or month == "Dec":#Checks if the month is equal to December or Dec
        print(calendar.month(yy,12))#If that is the case it prints the calendar for December in the specified year
    else:
        print("An error occurred please run python <module name> -h to see the utilisation manual")

#Here we create the banner that will be shown when the -h argument is passed
def banner():
    print("*" * 50)
    print("For the system to work enter the month's name fully or using their abbreviation")
    print("For example: ")
    print("Enter month: January or Enter month: Jan")
    print("Enter year: 2022")
    print("NOTE THAT MAY doesn't have an abbreviation")
    print("")
    print("*" * 50)
    print("")


if len(sys.argv) == 1: #Checks if the sys.arg array contains only one item
#if the array contains 1 item only the following code is ran
    month = input("Enter month: ")#Prompts the user to enter a month
    yy = int(input("Enter year: ")) #Prompts the user to enter a year
    printCalendar(month, yy)# Calls the printCalendar function and passes the arguments
elif len(sys.argv) == 2 and sys.argv[1] == "-h":
#The line above checks if the sys.argv array 2 items and if the second item is a "-h" which is passed when the module is ran
#The that is the case the banner function is called
    banner()
    month = input("Enter month: ")
    yy = int(input("Enter year: "))
    printCalendar(month)
