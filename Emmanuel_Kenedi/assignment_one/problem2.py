"""
Python has a built in function called calendar() that displays the calenderfor a given month and year. It accepts integer inputs. I wanted to allow the user to enter the name of the month instead of the number hence the custom function clndr() which contains a dictionary of months with names as keys and month numbers as values. -Emmanuel Kenedi, 2022
"""

import calendar

def clndr(y, m):
	m = m.casefold()
	months = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
	
	for x in months:
		if x == m:
			m = months.get(x)
			print(calendar.month(y, m))

print("Calender App by Emmanuel Kenedi \n\n")
month = input("Enter month: ")
year = int(input("Enter year: "))
clndr(year, month)