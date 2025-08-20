from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scoreboard
from wall import Wall
import time

accuracy = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scorecard = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = False

def start_game():
    global game_running
    scorecard.reset_score()
    scorecard.clear()
    scorecard.update_scoreboard()
    snake.reset()
    wall.clear_walls()
    food.refresh()
    game_running = True
    run_game()

def restart_game():
    global game_running
    scorecard.reset_score()
    scorecard.clear()
    scorecard.update_scoreboard()
    snake.reset()
    wall.clear_walls()
    food.refresh()
    game_running = True
    run_game()

def run_game():
    global game_running
    while game_running:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #handling stages
        if scorecard.score >= 10 and scorecard.score < 25:
            wall.create_fixed_walls()
        elif scorecard.score >= 25:
            if not wall.segments:
                wall.create_random_walls(count=10)

        #collision with food
        if snake.all_turtles[0].distance(food) < accuracy:
            food.refresh()
            snake.extend()
            scorecard.increase_scoreboard()
            if scorecard.score >= 25:
                wall.create_random_walls(count=10)

        #collision with wall
        for w in wall.segments:
            if snake.all_turtles[0].distance(w) < 15:
                scorecard.game_over()
                game_running = False

        #collision with screen border
        if (snake.all_turtles[0].xcor() > 290 or snake.all_turtles[0].xcor() < -290 or
            snake.all_turtles[0].ycor() > 280 or snake.all_turtles[0].ycor() < -280):
            scorecard.game_over()
            game_running = False

        #collision with tail
        for turtle in snake.all_turtles[1:]:
            if snake.all_turtles[0].distance(turtle) < 10:
                scorecard.game_over()
                game_running = False

screen.onkey(start_game, "space")
screen.onkey(restart_game, "r")

scorecard.start_message()

screen.exitonclick()
