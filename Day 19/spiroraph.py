import turtle as t
from random import randint
t.colormode(255)
tim=t.Turtle()
tim.pensize(2)
tim.speed("fastest")
# tim.setpos(0,0)
# tim.shape("circle")
screen=t.Screen()
screen.setup(1280,1080)

def random_color():
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	random_color=(r,g,b)
	return random_color

radius=100
def draw_graph(size_of_gap):
	for i in range(int(360/size_of_gap)):
		tim.circle(radius)
		tim.color(random_color())
		tim.setheading(tim.heading()+size_of_gap)

draw_graph(int(input("Enter the size of the gap: ")))

screen.exitonclick()