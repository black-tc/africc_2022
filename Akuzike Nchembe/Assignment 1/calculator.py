
def calculate(problem):
    """
    This function calculates any sum given with basic math operators
    e.g 23+56-98*8
    """
    counter = 0
    operators = []

    #Getting the indexes of the operators in the string
    for op in problem:
        if op == '/' or op == '*' or op == '+' or op == '-':
            operators.append(counter)
        counter += 1
        
    answer = float(problem[0:operators[0]])
    num2 = 0
    track = 1

    #Extracting numbers in the problem
    for x in operators:

        if x != (operators[-1]):
            num2 = float(problem[x+1:operators[track]])
            track += 1
        else:
            num2 = float(problem[x+1:])

        #calculating solution
        if problem[x] == '/':
            answer = answer / num2
        elif problem[x] == '*':
            answer = answer * num2
        elif problem[x] == '+':
            answer = answer + num2
        elif problem[x] == '-':
            answer = answer - num2

    return answer
    

answer = input("Enter a sum: ")
answer = calculate(answer)
print(answer)
