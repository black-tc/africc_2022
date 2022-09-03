'''
Problem 2: Obtain user input and try to display the calendar for that month
'''

import calendar

user_year = int(input("Input the year: "))
user_month = input("Input the month: ")
user_month = user_month.capitalize()

for month in range(1, 13):
    if int(user_month) == month or user_month == calendar.month_name[month] or user_month == calendar.month_abbr[month]:
        print(calendar.month(user_year, month))
    