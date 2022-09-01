
import calendar

year = input("Please enter year: ")
month = input("Please enter month: ")

while int(month) < 0 or int(month) > 12:
    print("Invalid Input!! Value has to be between 0<x<13")
    month = input("Please enter valid month number: ")

print(calendar.month(int(year), int(month)))