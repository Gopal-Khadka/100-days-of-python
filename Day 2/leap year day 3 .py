#leap year
year = int(input("ENTER THE YEAR YOU WANT TO CHECK:\n"))
message1 = f"Year {year} is a leap year."
message2 = f"Year {year} is not a leap year."

if year%4==0:
	if year%100==0:
		if year%400==0:
			print(message1)
		else:
			print(message2)
	else:
		print(message1)
else:
	print(message2)