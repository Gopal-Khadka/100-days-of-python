#highest mark finder
student_marks=input("Enter a list of student scores:\n").split()
for n in range(0,len(student_marks)):
	student_marks[n]=int(student_marks[n])

highest_mark=0
for marks in student_marks:
	if(marks > highest_mark):
		highest_mark = marks
print(f"The highest score is: {highest_mark}")