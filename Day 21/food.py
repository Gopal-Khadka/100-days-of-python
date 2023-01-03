from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        x_pos=randint(-280,280)
        y_pos=randint(-280,280)
        self.goto(x_pos,y_pos)
