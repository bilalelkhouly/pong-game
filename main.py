# Pong Game

import time
from turtle import Screen
from ball import Ball
from center_line import CenterLine
from paddle import Paddle
from scoreboard import Scoreboard
from exit_button import Button
from winner import Winner

LEFT_PADDLE_POSITION = (-350, 0)  # Paddle position
RIGHT_PADDLE_POSITION = (350, 0)
LEFT_SCOREBOARD_POSITION = (-100, 200)  # Scoreboard position
RIGHT_SCOREBOARD_POSITION = (100, 200)

screen = Screen()   # Create a screen object
screen.setup(width=800, height=600) # Set the screen size
screen.bgcolor("black") # Set the background color
screen.title("Pong Game")   # Set the title of the screen
screen.tracer(0)

game_is_on = True   # Set the game state

right_paddle = Paddle(RIGHT_PADDLE_POSITION)    # Create a paddle object
left_paddle = Paddle(LEFT_PADDLE_POSITION)

ball = Ball()
center_line = CenterLine()
exit_button = Button("Exit", (0, -290))     # Create an exit button
button_length = 50
button_width = 50
left_scoreboard = Scoreboard(LEFT_SCOREBOARD_POSITION)      # Create a scoreboard object
right_scoreboard = Scoreboard(RIGHT_SCOREBOARD_POSITION)
winner = Winner()

screen.listen()    # Listen for key presses
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


def is_clicked(x, y):
    if (exit_button.xcor() - button_length <= x <= exit_button.xcor() + button_length and   # Check if the exit button is clicked
            exit_button.ycor() - button_length <= y <= exit_button.ycor() + button_width):
        winner_text = 0 if left_scoreboard.score > right_scoreboard.score \
            else 1 if right_scoreboard.score > left_scoreboard.score \
            else 2
        winner.write_winner(winner_text)    # Write the winner text
        center_line.clear()
        ball.clear()
        screen.exitonclick()    # Exit the screen


while game_is_on:
    time.sleep(ball.moving_speed)   # Set the speed of the ball
    screen.update()    # Update the screen
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect ball collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
            left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect when ball goes out of bounds for left player
    if ball.xcor() > 390:
        left_scoreboard.update_scoreboard()
        ball.reset_position()

    # Detect when ball goes out of bounds for right player
    if ball.xcor() < -390:
        right_scoreboard.update_scoreboard()
        ball.reset_position()

    screen.onclick(is_clicked)  # Check if the exit button is clicked
