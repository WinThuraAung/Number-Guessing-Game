from random import randint
from replit import clear
from art import logo


def numberGuessingGame():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100, inclusive.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        number_of_chances = 10
    elif difficulty == "hard":
        number_of_chances = 5

    while number_of_chances > 0:
        print(f"you have {number_of_chances} attempts left to guess the number")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too High!")
            print("Guess again")
        elif guess < number:
            print("Too Low!")
            print("Guess again")
        elif guess == number:
            print(f"You got it! The answer was {number}.")
            break
        number_of_chances -= 1

    print("Game Over")


while input("Do you want to play a number guessing game? Type 'y' or 'n': ") == "y":
    clear()
    numberGuessingGame()