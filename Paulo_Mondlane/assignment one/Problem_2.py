#!/usr/bin/env python
import calendar

calendar_ = lambda y,m: print(calendar.month(y, m))
y = int(input("Insert the year: "))
m = int(input("Insert the month(1-12): "))
calendar_(y,m)