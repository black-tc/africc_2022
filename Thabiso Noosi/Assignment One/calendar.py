# Program to display calendar of the given month and year

# importing calendar module
import calendar

#yy = 2014  # year
#mm = 11    # month

# To take month and year input from the user
print("Made by: Noosi")
print("_____________________")
print("Simple Calendar")
print("---------------------")
yy = int(input("Enter year: "))

mm = int(input("Enter month: "))

print("====================")
print(calendar.month(yy, mm))
