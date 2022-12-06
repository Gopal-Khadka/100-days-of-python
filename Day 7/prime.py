num=int(input("Enter the number to check:\n"))
def prime(n):
	is_prime=True
	for  i in range(2,n):
		if (n % i==0):
			is_prime=False
	if (is_prime):
		print(f"{n} is a prime number!!!")
	else:
		print(f"{n} is not a prime number!!!")
prime(n=num)