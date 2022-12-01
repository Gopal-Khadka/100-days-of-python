print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______//____/ _
*******************************************************************************
''')
message="Good luck next time!!!"
print("Welcome to the treasure island:")
print("Your goal is to find the hidden treasure.")
direction = input("You are at the crossroad.Where do you want to go? Type Left or Right.\n").lower()
if(direction=="left"):
	print("You are at the lake now.There is an island at the middle of the lake.")
	action1= input("Do you want to wait for boat or swim across the lake.Type Wait or Swim.\n").lower()
	if(action1=="wait"):
		print("You arrive at the island unharmed.")
		door=input("There are three doors in front of you. Which do you choose ? RED or BLUE or GREEN\n").lower()
		if(door=="green"):
			print("You got the treasure.You can go back home.")
		elif(door=="red"):
			print("You are burned by fire.")
			print(message)
		elif(door=="blue"):
			print("You are drowned by water.")
			print(message)
		else:
			print("The door doesn't exist.")
			print(message)
	else:
		print("You were eaten by crocodiles.")
		print(message)
else:
	print("You are killed by tigers.")
	print(message)