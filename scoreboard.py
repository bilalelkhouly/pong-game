from turtle import Turtle

FONT = ("EA Font v1.5 by Ghettoshark", 80, "normal")
ALIGNMENT = "center"


# Create a Scoreboard class that inherits from Turtle that is responsible for displaying the score
class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")  # Set the color of the text
        self.penup()  # Don't draw a line when moving
        self.goto(position)  # Move the score to position
        self.hideturtle()  # Hide the score
        self.update_scoreboard()  # Update the scoreboard

    def update_scoreboard(self):
        self.clear()  # Clear the previous text
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)  # Write the new score
        self.score += 1

    def game_over(self):
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))  # Write the game over text
