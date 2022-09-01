

print("Welcome to the calculator \nwhat operation would you like to perform?\n")
exit = False

# while loop to keep the program running
while exit == False:

    
    #this function is used to calculate additon
    def addition():
        print("Enter the numbers you would like to add seperated by a space:\n")
        numbers = input()
        numbers = numbers.split()
        
        total = 0
        try:
            for number in numbers:
                total += int(number)
            print("= " + str(total) +"\n\n")
        except:
            print("Invalid input")
            addition()
        
    #this function is used to calculate subtraction
    def subtraction():
        print("Enter the numbers you would like to subtract seperated by a space:\n")
        numbers = input()
        numbers = numbers.split()
        
        total = int(numbers[0])
        try:
            for number in numbers[1:]:
                total -= int(number)
            print("= " + str(total) +"\n\n")
        except:
            print("Invalid input")
            subtraction()

    #this function is used to calculate multiplication
    def multiplication():
        print("Enter the numbers you would like to multiply seperated by a space:\n")
        numbers = input()
        numbers = numbers.split()
        
        total = 1
        try:
            for number in numbers:
                total *= int(number)
            print("= " + str(total) +"\n\n")
        except:
            print("Invalid input")
            multiplication()

    #this function is used to calculate division
    def division():
        print("Enter the numbers you would like to divide seperated by a space:\n")
        numbers = input()
        numbers = numbers.split()
        total = 0
        if numbers[1] == 0:
            print("You cannot divide by 0")
        else:
            try:
                total = float(numbers[0]) / float(numbers[1])
                print("= " + str(total) +"\n\n")
            except:
                print("Invalid input")
                division()


    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
    operation = input("Enter the operation you would like to perform: ")

    #this is the switch statement that will determine which operation to perform    
    if operation == "1":
        addition()
    elif operation == "2":
        subtraction()
    elif operation == "3":
        multiplication()
    elif operation == "4":
        division()
    elif operation == "5":
        print("Thank you for using the calculator")
        exit = True

