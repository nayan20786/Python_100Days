# Day12
import random

from art import GuessNumber_logo

print(GuessNumber_logo)

# To Do
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
Computer_Thought = random.randint(1, 101)
print(Computer_Thought)
difficulty = ""
while difficulty not in ["hard", "easy"]:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == "easy":
        guess = 10
    elif difficulty == "hard":
        guess = 5
    else:
        print("Choose the correct option for Difficulty")
user_guess = ""
while user_guess != Computer_Thought and guess > 0:
    user_guess = int(input("Make a guess"))
    if user_guess > Computer_Thought:
        print("Too high")
        guess = guess - 1
        print(f"you have {guess} guess remaining")
    elif user_guess < Computer_Thought:
        print("Too high")
        guess = guess - 1
        print(f"you have {guess} guess remaining")
    elif user_guess == Computer_Thought:
        print("Correct Guess! You read computers Mind")
    else:
        print("Invalid Input")
if guess == 0:
    print("You have lost")

exit()

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
