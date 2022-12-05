#hangman
from random import choice
from words import word_list
from logo import stages ,logo

chosen_word=choice(word_list)
word_length=len(chosen_word)
display=[]
game_end=False
lives = 6
print(logo)

for _ in range(word_length):
	display+="_"
	
while not game_end:
	guess=input("Enter your guess word:").lower()
	
	for position in range(word_length):
		letter=chosen_word[position]
		
		if letter == guess:
			display[position]=letter
			
	if guess not in chosen_word:
		lives -=1
		if lives==0:
			game_end=True
			print("\nYou lose!!!")
		
	print(stages[lives])
	final=" ".join(display)
	
	if not lives==0:
		print(final)
		
	if "_" not in display:
		game_end=True
		print("\nYou won!!!")
		
print(f"The word was {chosen_word}.")