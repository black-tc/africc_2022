import calendar #importing the calendar module

print() #linebreak

print("Program to display the calendar for a particular month") #displaying the use for this program

print() #printing a line break

#Giving the user the information that can be input into the program
print("January = 1")
print("February = 2")
print("March = 3")
print("April = 4")
print("May = 5")
print("June = 6")
print("July = 7")
print("August = 8")
print("September = 9")
print("October = 10")
print("November = 11")
print("December = 12")

print() #printing a line break

#Asking the user for the input
mm= int(input("Please write the number associated with your desired month: "))
yy = int(input("Please write the year: "))

print() #linebreak

#the calendar module
print(calendar.month(yy, mm))

