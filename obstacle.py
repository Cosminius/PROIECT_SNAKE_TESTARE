from turtle import Turtle
import random

#Obsolete mi-a dat crash si am sters implementarrea


class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-260, 260), random.randint(-260, 260))