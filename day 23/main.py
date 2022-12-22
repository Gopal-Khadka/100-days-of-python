from turtle import Turtle,Screen
from scoreboard import Scoreboard
from car import Car
import time
from tortoise import Tortoise

screen=Screen()
screen.setup(600,600)
screen.tracer(0)
player=Tortoise()
car=Car()
score=Scoreboard()


screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.cars_move()
    # detect collision with car of turtle
    for cars in car.all_cars:
        if cars.distance(player) < 19:
            game_is_on=False
            score.game_over()

    # detect success of crossing
    if player.is_over_finish():
        player.reset_position()
        car.level_up()
        score.increase_level()

screen.exitonclick() 