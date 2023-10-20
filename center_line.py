from turtle import Turtle

WIDTH = 4
DASH_LENGTH = 10
INTERVAL = 20


# Create a CenterLine class that inherits from Turtle and shows the center line
class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.width(WIDTH)
        for distance in range(-230, 300, INTERVAL):
            self.penup()
            self.goto(0, distance)
            self.pendown()
            self.goto(0, distance + DASH_LENGTH)
