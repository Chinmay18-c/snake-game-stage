import random
from turtle import Turtle

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []

    def add_walls(self, position):
        wall_piece = Turtle("square")
        wall_piece.color("red")
        wall_piece.shapesize(stretch_wid=1, stretch_len=1)
        wall_piece.penup()
        wall_piece.goto(position)
        self.segments.append(wall_piece)

    def create_fixed_walls(self):
        self.clear_walls()
        positions = [(0,100),(0,-100),(100,0),(-100,0)]
        for i in positions:
            self.add_walls(i)

    def create_random_walls(self, count=6):
        self.clear_walls()
        for i in range(count):
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            self.add_walls((x,y))

    def clear_walls(self):
        for wall in self.segments:
            wall.hideturtle()
        self.segments.clear()
