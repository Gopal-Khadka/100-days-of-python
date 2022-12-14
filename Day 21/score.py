from turtle import Turtle
ALIGN="center"
FONT=("Ubuntu",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0,260)
        self.update_score()

    def scoreBoard(self):
        self.score+=1
        self.clear()
        self.update_score()
       

    def update_score(self):
        self.write(f"Score:{self.score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over",align=ALIGN,font=FONT)
