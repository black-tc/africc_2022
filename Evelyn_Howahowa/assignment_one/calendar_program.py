# Print calendar of the month using year and calendar for that month
# params: Year (int), Month (int)
# e.g. year = 1993, month = 7 for July,1993
# Author: Evelyn 
# 2 Sept, 2022

import calendar

year = eval(input("Enter year:\n> "))
month = eval(input("Enter month:\n> "))

print(calendar.month(year, month))