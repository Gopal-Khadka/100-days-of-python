import turtle
from random import choice,randint
directions=[0,90,180,270]
tim=turtle.Turtle()
tim.speed("fast")
turtle.colormode(255)

def change_color():
	color=["red","blue","yellow","green","purple","pink","brown","black","orchid"]
	return choice(color)

def random_color():
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	random_color=(r,g,b)
	return random_color

tim.pensize(10)
for _ in range(200):
	tim.fd(30)
	tim.setheading(choice(directions))
	tim.color(random_color())
	
screen=turtle.Screen()
screen.exitonclick