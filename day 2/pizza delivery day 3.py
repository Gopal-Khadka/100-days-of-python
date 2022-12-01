#pizza delivery
print("Welcome to the Pizza Bazzar.")
size = input("What size pizza do you want? S , M or L\n")
add_pepperoni = input("Do you want pepperoni? Y for yes and N for no\n")
extra_cheese = input("Do you want extra cheese? Y for yes and N for no\n")
bill = 0

if size == "s" or size =="S":
	bill += 15
elif size == "m" or size =="M":
	bill += 20
else :
	bill += 25
if add_pepperoni == "Y" or add_pepperoni=="y":
	if size == "s" or size =="S":
		bill +=2
	else:
		bill +=3
if extra_cheese == "Y" or extra_cheese == "y" :
	 bill+=1
print(f"Your final bill is ${bill}.")