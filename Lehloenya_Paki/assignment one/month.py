#!/usr/bin/python3

import calendar

year = int(input("Enter the year: "))
mth = int(input("Enter the month: "))


if mth >= 1 and mth <= 12:
    print(calendar.month(year,mth))
else:
    print("This month does not exist")
