import os,time
from art import logo 
 
 
def fibonacci(num):
	Fibonacci_series=[0,1]
	if num==1:
		return ([Fibonacci_series[0]])
	elif num==2:
		return (Fibonacci_series)
	else:
		for i in range(num-2):
			new_num=Fibonacci_series[-2]+Fibonacci_series[-1]
			Fibonacci_series.append(new_num)
		return (Fibonacci_series)

def fibonacci_finder(num):
	a = 0
	b = 1
	fibonacci_list=[a,b]
	while num>b:
		c = a+b
		a = b
		b = c
		fibonacci_list.append(a)
	return (fibonacci_list)


def check_fibonacci(num):
    a = 0
    b = 1
    while num>b:
        c = a+b
        a = b
        b = c
    if b==num or a==num:
        return True
    if b > num:
        return False

def fibonacci_app():
	print(logo)
	print("Welcome to the fibonacci app.")
	print("What do you want me to do:")
	option=int(input("Enter:\n\t(1) for fibonacci series\n\t(2) for fibonacci check\n\t(3) for fibonacci between two numbers\n"))

	if option==1:
		num=int(input("Enter no of items in fibannoci series you want: "))
		print(fibonacci(num))
	elif option==2:
		num=int(input("Enter the number you want to check: "))
		if check_fibonacci(num):
		    print(f"{num} is a fibonacci number.")
		else:
		    print(f"{num} is not a fibonacci number.")
	elif option==3:
		print("Enter numbers of which you want fibonacci numbers.")
		low_num=int(input("Enter the lower number: "))
		high_num=int(input("Enter the higher number: "))
		list_of_num=[]
		for num in fibonacci_finder(high_num):
			if low_num<=num<=high_num:
				list_of_num.append(num)
		print(list_of_num)
	else:
		print("The entered option is invalid.")
		time.sleep(2.5)
		os.system('cls')
		fibonacci_app()

fibonacci_app()
while input("Enter Yes(Y) to use app again or No(N) to quit app: ").lower() in ["y","yes"]:
	os.system('cls')
	fibonacci_app()
print("Come back soon !!! ")