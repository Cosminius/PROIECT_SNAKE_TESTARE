from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#Declara global sa il folosim in toate loop-urile
#Trebuia facuta inca o clasa pentru interfata da nu imi pasa

game_is_on = False
def start_game():
    global game_is_on
    game_is_on = True
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()

        # Detecteaza mancare
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.expansion()
            scoreboard.increase_score()

        # Detecteaza zid
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = False
            scoreboard.game_over()

        # Detecteaza coada
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.bye()

def quit_game():
    screen.bye()

# Setup main menu
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Snake Game")

# Creare buuton play
play_button = Turtle()
play_button.penup()
play_button.hideturtle()
play_button.shape("square")
play_button.color("white")
play_button.shapesize(stretch_wid=1, stretch_len=3)
play_button.goto(0, 50)
play_button.write("Play", align="center", font=("Arial", 24, "normal"))
play_button.showturtle()

# Creare buton quit
quit_button = Turtle()
quit_button.penup()
quit_button.hideturtle()
quit_button.shape("square")
quit_button.color("white")
quit_button.shapesize(stretch_wid=1, stretch_len=3)
quit_button.goto(0, -50)
quit_button.write("Quit", align="center", font=("Arial", 24, "normal"))
quit_button.showturtle()

# Functie de testat butoanili
def check_click(x, y):
    if -50 < x < 50 and 25 < y < 75:
        play_button.hideturtle()
        quit_button.hideturtle()
        start_game()
    elif -50 < x < 50 and -75 < y < -25:
        quit_game()

screen.onclick(check_click)
screen.listen()
screen.mainloop()
