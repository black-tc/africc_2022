# import calendar module used to display calender format
import calendar

# obtain user input (year and month)
year = input("Enter year: ")
month = input("Enter month number: ")

# validate month
while int(month) < 0 or int(month) > 12:
    print("INVALID MONTH NUMBER")
    month = input("Enter valid month number: ")

# Display calendar to user
print(calendar.month(int(year), int(month)))