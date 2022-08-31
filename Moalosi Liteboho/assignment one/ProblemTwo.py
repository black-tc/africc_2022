import os  # Importing the module named os


def main():
    while True:
        month = int(input("Enter the month in number: "))  # Accepting the month as int from the user and store it in a variable
        year = int(input("Enter the year: "))  # Accepting the year as int from the user and store it in a variable

        if 0 < month <= 12:  #  If-statement that checks if the value in month is greater than zero and less than or equal to 12
            print("\nDisplaying Month Calender: \n")  # The statement that print message before displaying calender month
            month_calender = os.system("cal " + str(month) + " " + str(year))  # Statement that store bash command in a variable that will be runned when it is invocked 
            print(month_calender)  # The statement that print the callender month by invocking the variable that will run bash command

        choice = input("Do you want to use the program again? : \nChoice > ")  # Accepting user input

        if choice.lower().startswith("y"):  # Check user input whether it start with y for yes, run code if it is
            continue  # Loop again
        break  # Break while loop if if-statement didn't get executed


if __name__ == '__main__':
    main()
