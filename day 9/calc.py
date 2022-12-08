#Calculator
from logo import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
  
def modulo(n1, n2):
  return n1 % n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%":modulo
}

def calculator():
	end=False
	num1 = float(input("What's the first number?: "))
	for symbol in operations:
	  print(symbol)
	  
	while not end:
		operation_symbol = input("Pick an operation : ")
		num2 = float(input("What's the next number?: "))
		calculation_function = operations[operation_symbol]
		answer = round(calculation_function(num1, num2),2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		again=input(f"Type yes to do operation with {answer} or no to start new calculation: ").lower()
		if again=="yes":
			num1=answer
		else:
			end=True
			print("\n")
			calculator()
			
calculator()