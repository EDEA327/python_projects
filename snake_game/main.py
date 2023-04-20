import time
from turtle import Screen

from snake import Snake
from food import Food

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
        print("Collision detected")

# Keep the window open
screen.exitonclick()




