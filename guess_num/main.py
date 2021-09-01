# Number Guessing Game Objectives:
from random import randint
# Include an ASCII art logo.
from ascii import logo
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_number(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def check_difficulty(level):
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("-------------------------")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print("-------------------------")
    answer = randint(1, 100)
    turns = check_difficulty(level)
    guess = 0

    while guess != answer:
        print(f"You currently have {turns} reminding.")

        guess = int(input("Make your guess: "))

        turns = check_number(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses, you lost!!")
            print(f"The answer was {answer}!!")
            return
        else:
            print("Guess again!")


game()
