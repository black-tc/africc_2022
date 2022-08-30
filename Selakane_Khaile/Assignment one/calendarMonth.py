#Author: Selakane Khaile
#Date: 08/30/2022

import calendar

year=2022 #give the current year 

mm=int(input("Enter a month nuber: ")) #get user input
if mm > 0 and mm < 13:                 #validate month range
    print(calendar.month(year,mm))     #print moth of year inserted
else:
    print ("Plese insert valid month number!")
