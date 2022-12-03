#average height calc
heights=input("Enter the height of the students: \n").split()
i,sums=0,0
for height in heights:
	sums+=int(height)
	i+=1
avg = round(sums/i)
print(f"the average height of the student is {avg}")