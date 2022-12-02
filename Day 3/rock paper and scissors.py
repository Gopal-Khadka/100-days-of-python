#jan ken pop
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
win="You win!"
lose="You lose!"
error="You chose invalid number."
choice1="You chose:\n"
choice2="Computer chose:\n"
game_signs=[rock,paper,scissor]
user_input=int(input("Enter 0 for rock , 1 for paper and 2 for scissors:\n"))
if(user_input>=3) or (user_input<0):
	print(error + lose)
else:
	print(choice1)
	print(game_signs[user_input])
	computer=random.randint(0,2)
	print(choice2)
	print(game_signs[computer])

	if (user_input==0) and (computer==2):
		print(win)
	elif (user_input==2) and (computer==0):
		print(lose)
	elif(user_input> computer):
		print(win)
	elif(user_input< computer):
		print(lose)
	else:
		print("It's a draw.")
		