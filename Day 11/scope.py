#scope
#wrong way
# enemies=1

# def increase_enemies():
# 	enemies+=1
# 	print(enemies)

# increase_enemies()
# print(enemies)

#right way
enemies=1

def increase_enemies():
	global enemies
	enemies+=1
	print(enemies)

increase_enemies()
print(enemies)


#moding values withut modifying global variable
#note: global variables' value should not be changed.It makes confusion in program.
#Note: Use all capital letters to define constant as convention
PI = 3.14
enemies=1

def increase_enemies():
	global enemies
	return enemies+1

increase_enemies()
print(enemies)



