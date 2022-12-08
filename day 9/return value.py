
def format_name(first_name,last_name):
	"""Returns formatted name of user"""
	first_name=first_name.title()
	last_name=last_name.title()
	fullname=first_name +" "+last_name
	return fullname 	#return keyword ends the function
	print(True)
	
	
name=input("Enter your first name: ")
surname=input("Enter your last name: ")

fullname=format_name(name,surname)
print(f"Your formatted name is {fullname}.")
