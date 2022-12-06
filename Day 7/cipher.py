from logo import logo

print(logo)
end=False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
			'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] *2

def caesar(plain_text,shift_num,direction):
		final_word="" 
		shift_num = shift_num % 25
		
		if direction == "decode":
				shift_num *= -1
				
		for char in text:
			if char in alphabet:
				position=alphabet.index(char)
				new_position = position + shift_num
				final_word+=alphabet[new_position]
				#all above 3 lines can be written as:
				#FINAL+=alphabet[alphabet.index(char) + shift_num]
			else:
				final_word+=char
		print(f"\nThe {direction}d text is {final_word}.")

while not end:
	cipher_direction=input("Enter 'encode' to encrypt or 'decode' to decrypt\n").lower()
	text = input("\nType your message: ").lower()
	shift = int(input("Type the shift number: "))
	
	caesar(plain_text=text,direction=cipher_direction,shift_num=shift)
	again=input("\nDo you want to run the program again.Enter 'Y' for yes or 'N' for no:\n ").lower()
	if again=="n":
		end=True
	elif again!= "y" or again!= "n":
		print("\nGiven value is invalid!!!")
		end=True