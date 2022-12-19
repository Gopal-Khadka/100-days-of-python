from turtle import Turtle,Screen
tim=Turtle()
tim.pensize(2)
tim.shape("turtle")
def forward():
    tim.fd(100)

def back():
    tim.backward(100)

def right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)

def left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.speed(("fastest"))
    tim.home()
    tim.pendown()

screen=Screen()
screen.listen()
"""Function as input needs no brackets"""
"""Higher order function"""
screen.onkey(fun=forward, key="w")
screen.onkey(fun=back, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
