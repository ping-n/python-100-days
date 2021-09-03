from art import logo
from art import vs
import random
from game_data import data
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def format_data(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f"{name}, a {description}, from {country}."


def get_random_data():
    return random.choice(data)


def check_answer(guess, account_a, account_b):
    if account_a > account_b:
        return guess == "A"
    else:
        return guess == "B"


def game():
    print(logo)
    score = 0
    account_a = get_random_data()
    account_b = get_random_data()
    game_continue = True

    while game_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        guess = input("Who have the most follower? Type A or B: ").capitalize()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        correct = check_answer(guess, a_follower_count, b_follower_count)

        clearConsole()
        print(logo)
        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            print("--------------")
        else:
            print(f"You lost! score: {score}")
            game_continue = False


# Start the game
game()
