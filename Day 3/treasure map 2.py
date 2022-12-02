#simple map for teasure
row1=["0","0","0"]
row2=["0","0","0"]
row3=["0","0","0"]
map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
user_input= input("enter row as first number and column as second number:\n")
x=int(user_input[0])
y=int(user_input[1])

if (x >3) or (y >3):
	print("Invalid values.")
else:
	selected_row=map[x-1]
	selected_row[y-1]="X"
	# map[x-1][y-1]="X"
	print(f"{row1}\n{row2}\n{row3}")