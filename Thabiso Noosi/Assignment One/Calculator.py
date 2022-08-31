# adding 
def add(x, y):
    return x + y

# subtracting
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

print ("Made by: Noosi")
print ("Simple Calculator")
print ("-----------------")
print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("__________________")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
       
        next_calculation = input("Continue Calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")