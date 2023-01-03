from art import *
from gamedata import data
import random
def random_contestant():
	index=random.randint(0,len(data)-1)
	return index

def description(index):
	"""returns description of contestant"""
	job=data[index]['description']
	country=data[index]['country']
	profile=f"{job} from {country}"
	return [profile]

def followers(index):
	"""returns follower count of contestant"""
	follower=data[index]['follower_count']
	return follower

def compare_follower(follower1,follower2):
	"""Compares follower of two contestant"""
	if follower1>follower2:
		return True
	else:
		return False

def next_contestant():
	index=random_contestant()
	contestant = data[index]['name']	
	profile=description(index)[0]
	follower=followers(index)
	return[index,contestant,profile,follower]



def high_low_game():

	print("Welcome to the higher-lower game:")
	print(logo)
	primary_contestant_data=next_contestant()
	print(f"Compare A: {contestant_data[1]},a {contestant_data[2]}.")
	print(vs)
	secondary_contestant_data=next_contestant()
	print(f"Compare B: {contestant_data[1]},a {contestant_data[2]}.")
	answer=input("Who mas more followers on instagram: ")
	compare(first_follower,second_follower)





high_low_game()
