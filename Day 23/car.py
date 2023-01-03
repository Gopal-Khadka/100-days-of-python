from turtle import Turtle
from random import choice, randint

RANDOM_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
MOVE_DISTANCE=5
MOVE_INCREMENT=7

class Car(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=MOVE_DISTANCE

    def create_car(self):
        rand_num=randint(1, 6)
        if rand_num ==1:
            new_car=Turtle(shape="square")
            new_car.color(choice(RANDOM_COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            rand_y=randint(-250, 250)
            new_car.goto(300,rand_y) 
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT

   