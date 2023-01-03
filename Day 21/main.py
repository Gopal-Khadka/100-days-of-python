from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Score
BOUNDARY=[-280,280]
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("yellow")
screen.title("Snake Game By Gopal Khadka")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
is_game_on=True
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while is_game_on:
    screen.update()
    sleep(0.2)
    snake.move()

    # detect collision of food and snake
    if snake.head.distance(food) <15:
        food.new_location()
        # extend snake body after food
        snake.extend_snake()
        score.scoreBoard()
      
    # detect collision with wall
    if snake.head.xcor()> 281 or snake.head.xcor() <-281 or snake.head.ycor() > 281 or snake.head.ycor()< -281:
        is_game_on=False
        score.game_over()
        
    # detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment)< 10:
            is_game_on=False
            score.game_over()


screen.exitonclick()