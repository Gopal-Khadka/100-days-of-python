from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game By Gopal Khadka")
screen.tracer(0)


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score=Score()
screen.listen()
screen.onkey(fun=r_paddle.Up, key="Up")
screen.onkey(fun=r_paddle.Down, key="Down")

screen.onkey(fun=l_paddle.Up, key="w")
screen.onkey(fun=l_paddle.Down, key="s")


is_game_on=True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # detect collision with up and down walls
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.ybounce()
    # detect collision with paddles
    # value of separation is 50 to solve hitting of ball at edge as distance is calculated from centres.
    if ball.xcor() >320 and ball.distance(r_paddle) <40 or ball.xcor() <-320 and ball.distance(l_paddle) <40 :
        ball.xbounce()

    # detect miss of r paddle
    if ball.xcor()>380 :
        ball.reset_position()

        score.l_score()
        # detect miss of l paddle
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_score()



screen.exitonclick()
