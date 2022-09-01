
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

print ("Welcome to calculator app v1.0 \n")
print("Please select desired operation  -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplcation\n" \
        "4. Division\n")

select = int(input("Choose Option:"))
 
val_1 = int(input("Input first number: "))
val_2 = int(input("Input second number: "))
 
if select == 1:
    print(val_1, "+", val_2, "=",
                    add(val_1, val_2))
 
elif select == 2:
    print(val_1, "-", val_2, "=",
                    subtract(val_1, val_2))
 
elif select == 3:
    print(val_1, "*", val_2, "=",
                    multiply(val_1, val_2))
 
elif select == 4:
    print(val_1, "/", val_2, "=",
                    divide(val_1, val_2))
else:
    print("Invalid Input!! Rerun Program")