import random
import os
from logo import *

def compare(guess_num,correct_num):
	print("\n")
	if guess_num>correct_num:
		print("Guess is too high.")
	elif(guess_num<correct_num):
		print("Guess is too low.")
	elif(guess_num==correct_num):
		print("Your guess is correct.")

def game():
	print(logo)
	easy=["e","easy"]
	hard=["h","hard"]
	print("Welcome to higher or lower guessing number game.")
	level=input("Enter the level of game: Easy(E) or Hard(H)\n").lower()
	answer=random.randint(1,100)
	guess=int(input("Enter your guess number between 0 and 100: "))
	chances=0
	if level in easy:
		chances=9
	elif level in hard:
		chances=4
	compare(guess,answer)
	while chances>0:
		new_guess=int(input("Enter  your guess again: "))
		compare(new_guess,answer)
		if new_guess==answer:
			break
		chances-=1
		if chances==0:
			print("\nYou are out of attempts.")

game()

repeat=input("\nEnter yes(y) to play again or not(n) to quit:").lower()
while repeat=="y":
	os.system('cls')
	game()
