#heads or tails
import random
test_seed = input("Enter any desired seed number:\n")
random.seed(test_seed)

random_side = random.randint(0,1)
if(random_side==1):
	print("Heads")
else:
	print("Tails")