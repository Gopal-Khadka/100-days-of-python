#bmi calc v2.0

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi=int(weight / height**2)
print(f"Your bmi is {bmi}.")
response = ["underweight", "normal weight","overweight", "obese","clinically obese"]
if float(bmi) < 18.5 :
	print(f"You are {response[0]} ")
elif bmi < 25 :
	print(f"You are {response[1]} ")
elif float(bmi) < 30 :
	print(f"You are {response[2]} ")
elif float(bmi) < 35 :
	print(f"You are {response[3]} ")
else :
	print(f"You are {response[-1]} ")