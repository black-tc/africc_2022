# Program that obtain user input and display the calendar for that month and year

# importing calendar module
import calendar

# getting month and year input from the user
Year = int(input("Enter the year in digits: "))
Month = int(input("Enter the month number: "))

# displaying the calendar
print(calendar.month(Year, Month))