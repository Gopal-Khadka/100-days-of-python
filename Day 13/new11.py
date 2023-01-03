from random import choice
import os
from art import *
from gamedata import data

def random_contestant():
	"""Returns random data of contestant from the "data" list."""
	return choice(data)

def formatted_output(option):
	"""Returns formatted sentence for selected choices informing name,job and nation."""
	return f"{option['name']}, a {option['description']} from {option['country']}"

def compare(follower_a,follower_b,guess):
	'''Takes three parameters as input to compare followers and compare answer with user guess and returns either True or False'''
	if follower_a>follower_b:
		return guess=='a'
	else:
		return guess=="b"

def high_low_game():
	"""Main function where actual game starts."""
	answer=True
	score=0
	print('Welcome to the higher lower game.')
	print(logo)
	option_a=random_contestant()

	while answer:
		if score>0:
			print(f"You got it right. Your score: {score}")
		option_b=random_contestant()
		print(f"Compare A: {formatted_output(option_a)} with {option_a['follower_count']}M followers")
		print(vs)
		print(f"Compare B: {formatted_output(option_b)} with {option_b['follower_count']}M followers")
		guess=input("Who has more followers on Instagram? Type'A' or 'B': ").lower()
		answer=compare(option_a['follower_count'],option_b['follower_count'],guess)
		# Note: answer is also defined above in while loop. If answer here gets false, while loop also stops.
		#gives 3 arguments to compare to receive value as either True or False for below code execution
		if answer:
			score+=1
			option_a=option_b
		os.system('cls')
		print(logo)
	# prints final score if user enters wrong value.
	print(f"You are wrong! Your final score: {score}")
	while input("Do you want to play again? Type Yes(y) or No(n): ").lower() in ["y","yes"]:
		os.system('cls')
		high_low_game()
	print("Come back soon!!!")
	return

high_low_game()