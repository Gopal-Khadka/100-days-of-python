from turtle import Turtle
FINISH_LINE_Y=280
MOVE_DISTANCE = 10
STARTING_POSITION=(0,-280)


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_over_finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False