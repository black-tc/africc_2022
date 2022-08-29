"""
@author: Junior Moremong
description: Program that reads month from user input and displays its calendar
"""
import calendar

mm = int(input("Enter month (mm):")) #get month from the user
year = 2022 #year

print(calendar.month(year, mm))
