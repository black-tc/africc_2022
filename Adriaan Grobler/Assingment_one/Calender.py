
import math
import calendar

print("Welcome to the calender")
date = input("Enter a date in the format MM/YYYY: ")
date = date.split("/")

yearVal = int(date[1])
monthVal = int(date[0])

print(calendar.month(yearVal, monthVal))
