from logo import *
import random


def deal_card():
	"""Returns card each time it is called"""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]	
	card=random.choice(cards)
	return card

def calculate_score(list_of_card):
	'''Gives the sum of list of cards given following to certain game conditions.'''
	if sum(list_of_card)==21 and len(list_of_card)==2:
		return 0
	elif sum(list_of_card) > 21 and 11 in list_of_card :
		list_of_card.remove(11)
		list_of_card.append(1)
		return sum(list_of_card)
	else:
		return sum(list_of_card)

def compare(user,computer):
	"""Compare the values of user and computer and declare winner or loser following game rules."""
	if user==computer:
		print("It's a draw.")
	elif computer==0:
		print("Computer win!!")
	elif user==0:
		print("You win!!")
	elif computer>21:
		print("Computer lose!!")
	elif user>21:
		print("You lose!!")
	elif computer>user:
		print("Computer win!!")
	else:
		print("You win!!")

def play_game():
	print(logo)
	game_end=False
	user_card=[]
	computer_card=[]
	repeat=True

	while repeat:

		for i in range(2):
			"""Append two cards in user and computer cards list"""
			user_card.append(deal_card())
			computer_card.append(deal_card())


		while not game_end:
			user_score=calculate_score(user_card)
			computer_score=calculate_score(computer_card)
			print(f" Your cards are {user_card} and score is {user_score}")
			print(f" Computer cards are {computer_card[0]} ")

			if user_score>21 or user_score ==0 or  computer_score==0:
				game_end=True
				print("\nGame over")
			else:
				again=input("Enter'y' to draw another card or 'n ' to end game.").lower()
				if again in ["y","yes"]:
					user_card.append(deal_card())
		
				else:
					game_end=True

		while computer_score<17 and computer_score!=0 :
			computer_card.append(deal_card())
			computer_score=sum(computer_card)


		print(f" Your cards are {user_card} and score is sum(user_card).\n")
		print(f" Computer cards are {computer_card} and score is sum(computer_card).\n ")

		compare(user_score,computer_score)

play_game()
repeat_action=input("\nDo you want another game? Type 'Y' for yes or 'N' for no: ").lower()
while repeat_action in ["y","yes"]:
	play_game()

print("Have a good time!!")
 