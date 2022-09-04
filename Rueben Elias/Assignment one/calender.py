# Author: Rueben Elias
# Date: 31 August 2022
# Project Description: Display a Monthly Calender
import calendar
 
# take year from user
year = int(input("Enter Year: "))
 
# take month from user
month = int(input("Enter Month: "))
 
# printing Calendar
print(calendar.month(year, month))