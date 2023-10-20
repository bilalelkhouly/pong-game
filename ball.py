from turtle import Turtle


# Create a Ball class that inherits from Turtle and represents the ball
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1 / 2, stretch_len=1 / 2)
        self.penup()
        self.goto(0, 0)
        self.x_speed = 8
        self.y_speed = 8
        self.moving_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_speed *= -1

    def bounce_paddle(self):
        self.x_speed *= -1
        self.moving_speed *= 0.7

    def reset_position(self):
        self.goto(0, 0)
        self.moving_speed = 0.1
        self.bounce_paddle()
