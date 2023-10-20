from turtle import Turtle

FONT = ("EA Font v1.5 by Ghettoshark", 50, "normal")
ALIGNMENT = "center"


# Create a Button class that inherits from Turtle and shows the exit button
class Button(Turtle):

    def __init__(self, text, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.write(text, align=ALIGNMENT, font=FONT)
        self.text = text
        self.position = position