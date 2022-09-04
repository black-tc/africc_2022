import calendar

def month_calender(month,year):
    """
    This function takes the month of the year and prints the calender of that month
    """
    print("\n")
    calendar.prmonth(year,month)

year = int(input("Enter year (yyyy): "))
month = int(input("Enter month (mm): "))

month_calender(month,year)