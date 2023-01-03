scores={
	"Harry":90,
	"Gray":81,
	"Vim":99,
	"Sim":78,
	"Lee":65,
	"Tony":85
}
student_grades={}
for student in scores:
	score=scores[student]
	if score>90:
		student_grades[student]="Outstanding"
	elif 80< score <90:
		student_grades[student]="Good"
	elif 70<score<80:
		student_grades[student]="Acceptable"
	elif 70>score:
		student_grades[student]="Fail"


print(student_grades)