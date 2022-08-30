"""
This program can be written in 3 lines by using the eval() function. I refrained from that solution as the eval() function will run anything passed to it including commands. Using my custom calc() function, the expression is taken in as a string. calc() then searches for the operator within the string and extracts the operands which are then typecast into floats and operated upon depending on the found operator. -E.Kenedi, 2022
"""

def calc(expression):
	signs = ['+', '-', '/', '*', '^'] #Operators list
	for x in expression:
		if x in signs:
			v = expression.index(x) #Find the index of the operator to use as slicing point
			a = float(expression[0:v])
			b = float(expression[v+1:])
			if x == signs[0]:
				result = a+b
			elif x == signs[1]:
				result = a-b
			elif x == signs[2]:
				result = a/b
			elif x == signs[3]:
				result = a*b
			elif x == signs[4]:
				result = pow(a,b)
			else:
				print("UNSUPPORTED OPERATION!!!")
	return result
	
print("*-------Calculator by Emmanuel Kenedi-------*\n\n") #Splash screen
exp = input(":>> ")
print(calc(exp))