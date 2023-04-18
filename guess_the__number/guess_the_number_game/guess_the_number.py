import os
import random

from art import logo

#Functions
def clear():
    """Clear the console window"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_random_number():
    """ Return a random number between 1 and 100."""
    return random.randint(1,100)

def number_of_attempts(difficulty_level):
    attempts = 0

    if difficulty_level == "easy":
        attempts = 10
    elif difficulty_level == "hard":
        attempts = 5

    return attempts

def play_game():
    #Welcome to user
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking a number between 1 and 100.")
    #User choose a difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    #We give to user the number of attempts in function to difficulty level.
    attempts = number_of_attempts(difficulty)
    #The hidden number
    number = pick_random_number()
    # Looping until the number of attempts comes to zero
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        #Logic
        if number == guess:
            print("You win!")
            attempts = 0
        elif number > guess:
            print("Too low.")
            print("Please try again.")
            attempts -= 1
        else:
            print("Too high.")
            print("Please try again.")
            attempts -= 1

        if attempts == 0 and guess != number:
            print("You've ran out of attempts. You lose")
            print(f"The answer was {number}")

while input("Do you want to play guessing number game? (y/n): ").lower() == "y":
    clear()
    play_game()




















