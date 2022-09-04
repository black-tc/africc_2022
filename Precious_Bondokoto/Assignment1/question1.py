import operator 


op = {'+':operator.add,
      '-':operator.sub,
      '*':operator.mul,
      '/':operator.truediv}


num1 = int(input('Input 1st operand: '))
method = op[input('Input operator(+,-,*,/):')]
num2 = int(input('Input 2nd operand: '))

ans = method(num1,num2)
print('The answer is ', ans)