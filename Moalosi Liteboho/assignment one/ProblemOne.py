

def main():
    while True:
        results = 0
        is_calulated = True
        first_number = float(input("Enter the first number: "))  # Accepting user-input as float
        operating_sign = input("Enter the operating sign: ")  # Accepting the operatin sign that will determine what calculation to be done
        second_number = float(input("Enter the second number: "))  # Accepting user-input as float

        # The if-else statement that desired what operation to be done and do it and store the results in a results variable
        if operating_sign.__eq__("+"):
            results = first_number.__add__(second_number)
        elif operating_sign.__eq__("-"):
            results = first_number.__sub__(second_number)
        elif operating_sign.__eq__("*"):
            results = first_number.__mul__(second_number)
        elif operating_sign.__eq__("**") or operating_sign.__eq__("^"):
            results = first_number.__pow__(second_number)
        elif operating_sign.__eq__("/"):
            if second_number.__eq__(0):  # The if statement that checks if the divisor is equal to zero if yes print message and set is_calculated to false, OR else divide the dividend by divisor and store the value in results variable
                print("You can't divide " + first_number + " with 0. The result is undefined")
                is_calulated = False
            else:
                results = first_number.__divmod__(second_number)
        else:
            print("Invalid operating sign entered!!! \nTRY AGAIN !!!")

        if is_calulated:  # The if-statement that checks if the variable is_calculated is True and if yes print the Results
            print("RESULTS: \n" + str(first_number) + " " + str(operating_sign) + " " + str(second_number) +" = " + str(results))

        choice = input("Do you want to try to use calculator again (yes / no): ")  # Accept user-input whether user want to run code again

        if choice.lower().startswith("y"):  # Check user input whether it start with y for yes, run code if it is
            continue  # Continue to loop the while loop
        break  # Break out of the while loop


if __name__ == '__main__':
    main()
