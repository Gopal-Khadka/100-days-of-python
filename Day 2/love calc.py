#love calculator
#do you love me?????
print("Welcome to  the love calculator: ")
name1=input("Enter the first name:\n")
name2=input("Enter the second name:\n")
low_name1=name1.lower()
low_name2=name2.lower()
names= low_name1 + low_name2
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true = t+r+u+e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l+o+v+e
score = int(str(true) + str(love))
if (score <10) or (score > 90):
	print(f"Your love score is {score}. You go together like coke and mentos. ")
elif (score > 40) and (score < 50):
	print(f"Your love score is {score}. You go alright together.")
else:
	print(f"Your score is {score}.")