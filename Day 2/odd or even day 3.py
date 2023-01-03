#odd or even
#method 1
num1 = int(input(" Enter the number you want to check:\n"))
if num1 % 2==0:
	print("Your number is even.")
else:
	print("Your number is odd.")
print(("\n"))

#method 2
num2 = (input(" Enter the number you want to check:\n"))
if int(num2[-1]) % 2==0:
	print("Your number is even.")
else:
	print("Your number is odd.")