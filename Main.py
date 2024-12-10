
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from obstacle import Obstacle
from scoreboard import Scoreboard
import time
import tkinter as tk #Adaugat pentru input de nume
from tkinter import simpledialog

# Variabile globale pentru limba si joc
language = "EN"
game_is_on = False
highscores = []

# Dictionar pentru localizare
translations = {
    "EN": {
        "play_game": "Play Game",
        "quit_game": "Quit Game",
        "main_menu": "Main Menu",
        "team_name": "Created by Rosculet Cosmin, Stelic Ionut, Rus David, Pusok Alex - 2025",
        "choose_language": "Change Language",
        "enter_name": "Enter your name:"
    },
    "RO": {
        "play_game": "Incepe Jocul",
        "quit_game": "Iesi din Joc",
        "main_menu": "Meniu Principal",
        "team_name": "Creat de Rosculet Cosmin, Stelic Ionut, Rus David, Pusok Alex - 2025",
        "choose_language": "Schimba Limba",
        "enter_name": "Introdu numele tau:"
    }
}

# Creare butoane
play_button = Turtle()
quit_button = Turtle()
language_button = Turtle()
menu_button = Turtle()

# Cream o variabila stocare
player_name="Player"
obstacles = []
def generate_obstacle():
    global obstacles
    obstacle = Obstacle()
    obstacles.append(obstacle)
def change_language():
    global language
    language = "RO" if language == "EN" else "EN"
    show_menu()

def create_button(button, text, x, y):
    button.clear()
    button.hideturtle()
    button.shape("square")
    button.color("white")
    button.shapesize(stretch_wid=1, stretch_len=5)
    button.penup()
    button.goto(x, y)
    button.write(text, align="center", font=("Arial", 18, "bold"))

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.goto(-290, 290)
    border.pendown()
    border.pensize(3)
    border.color("white")
    for _ in range(4):
        border.forward(580)
        border.right(90)

def ask_player_name():
    global player_name
    root = tk.Tk()
    root.withdraw()  # Ascunde fereastra Tkinter
    player_name = tk.simpledialog.askstring("Input", translations[language]["enter_name"])
    if not player_name:
        player_name = "Player"

def show_menu():
    screen.clear()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.listen()

    # Creare butoane
    create_button(play_button, translations[language]["play_game"], 0, 120)
    create_button(quit_button, translations[language]["quit_game"], 0, 60)
    create_button(language_button, translations[language]["choose_language"], 0, 0)

    # Numele echipei si anul productiei
    writer = Turtle()
    writer.hideturtle()
    writer.color("white")
    writer.penup()
    writer.goto(0, -150)
    writer.write(translations[language]["team_name"], align="center", font=("Arial", 14, "italic"))

    # Activare click pentru butoane
    screen.onclick(check_click)

def check_click(x, y):
    if -60 < x < 60 and 100 < y < 140:
        ask_player_name()
        start_game()
    elif -60 < x < 60 and 40 < y < 80:
        exit_game()
    elif -60 < x < 60 and -20 < y < 20:
        change_language()

def exit_game():
    global game_is_on
    game_is_on = False
    screen.bye()

def start_game():
    global game_is_on
    game_is_on = True
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    draw_border()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()



    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    sleep_time=0.07
    while game_is_on:
        screen.update()
        time.sleep(sleep_time)
        snake.move_snake()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.expansion()
            scoreboard.increase_score()

        #Detectare coliziune cu peretii
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            game_is_on = False
            save_highscore(scoreboard.score)
            scoreboard.game_over()

        #Detectare coliziune cu coada
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                save_highscore(scoreboard.score)
                scoreboard.game_over()

    show_game_over_menu()

def save_highscore(score):
    global highscores
    found = False
    for index, (name, existing_score) in enumerate(highscores):
        if name == player_name:
            if score > existing_score:
                highscores[index] = (player_name, score)
            found = True
            break
    if not found:
        highscores.append((player_name, score))
    highscores = sorted(highscores, key=lambda x: x[1], reverse=True)[:5]

def show_game_over_menu():
    screen.clear()
    screen.bgcolor("black")
    writer = Turtle()
    writer.hideturtle()
    writer.color("white")
    writer.penup()
    writer.goto(0, 50)
    writer.write("Game Over", align="center", font=("Arial", 24, "bold"))

    if highscores[0][0] == player_name:
        writer.goto(0, 20)
        writer.write("🎉 New Highscore! 🎉", align="center", font=("Arial", 18, "bold"))

    create_button(play_button, translations[language]["play_game"], 0, -10)
    create_button(quit_button, translations[language]["quit_game"], 0, -50)
    create_button(menu_button, translations[language]["main_menu"], 0, -100)

    y_offset = -150
    for name, score in highscores:
        writer.goto(0, y_offset)
        writer.write(f"{name}: {score}", align="center", font=("Arial", 14, "normal"))
        y_offset -= 20

    screen.onclick(check_game_over_click)

def check_game_over_click(x, y):
    if -60 < x < 60 and -20 < y < 20:
        start_game()
    elif -60 < x < 60 and -70 < y < -30:
        exit_game()
    elif -60 < x < 60 and -120 < y < -80:
        show_menu()
    elif -60 < x < 60 and -20 < y < 20:
        change_language()
    elif -60 < x < 60 and -80 < y < -40:
        reset_highscore()

def reset_highscore():
    global highscores
    highscores = []

def save_highscore_to_file():
    with open("highscores.txt", "w") as file:
        for name, score in highscores:
            file.write(f"{name},{score}\n")

def load_highscore_from_file():
    global highscores
    try:
        with open("highscores.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                highscores.append((name, int(score)))
    except FileNotFoundError:
        highscores = []
load_highscore_from_file()





# Initializare ecran
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
show_menu()
screen.mainloop()
