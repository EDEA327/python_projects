import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off animation

# Create the initial snake
snake = Snake()

# Create the food
food = Food()

# Create the scoreboard
scoreboard = ScoreBoard()

# Event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Start the game
game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()
    # Add a small delay for the snake movement
    time.sleep(0.1)
    # Move the snake
    snake.move()
    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.change_position()
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.update_score()

# Keep the window open
screen.exitonclick()
