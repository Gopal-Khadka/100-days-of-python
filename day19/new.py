import turtle as t
from random import randint
screen=t.Screen()
is_race_on=False
screen.setup(width=500,height=500)
user_guess=screen.textinput(title="Turtle race", prompt="Which color do you pick: ")
colors=["red","violet","indigo","blue","yellow","green","orange"]
y_position=[0,40,-40,80,-80,120,-120]
turtle_list=[]

for turtle_no in range(0,7):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_no])
    new_turtle.penup()
    new_turtle.goto(x=-225,y=y_position[turtle_no])
    turtle_list.append(new_turtle)

if user_guess:
    is_race_on=True

def turtle_game():
    while is_race_on:
        for turtle in turtle_list:
            distance=randint(0, 10)
            turtle.pendown()
            turtle.fd(distance)
            if turtle.xcor()> 230:
                winning_color=turtle.pencolor()
                if winning_color==user_guess.lower():
                    print(f"You have won.The winning color is {winning_color}.")
                else: 
                    print(f"You have lost.The winning color is {winning_color}.")
                exit()
turtle_game()
screen.exitonclick()