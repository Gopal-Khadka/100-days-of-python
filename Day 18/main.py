from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
colors = ["red", "blue", "orchid", "yellow"] * 25
for i in range(100):
    tim.forward(100)
    tim.lt(90)
    tim.color(colors[i])

screen = Screen()
turtle.color("red")
screen.exitonclick()
