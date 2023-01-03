from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed=0.1


    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def ybounce(self):
        self.y_move*=-1

    def xbounce(self):
        self.x_move*=-1
        self.ball_speed*=0.9

    def reset_position(self):
        self.home()
        self.ball_speed=0.1
        self.xbounce()