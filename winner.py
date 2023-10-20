from turtle import Turtle

FONT = ("EA Font v1.5 by Ghettoshark", 50, "normal")
ALIGNMENT = "center"


# Create a Winner class that inherits from Turtle that shows the winner of the game
class Winner(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.hideturtle()

    def write_winner(self, winner):
        if winner == 0:
            self.write("Left Player wins!", align=ALIGNMENT, font=FONT)
        elif winner == 1:
            self.write("Right Player wins!", align=ALIGNMENT, font=FONT)
        else:
            self.write("Draw!", align=ALIGNMENT, font=FONT)
