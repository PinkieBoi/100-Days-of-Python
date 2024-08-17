import os
import random
from art import logo


def select_difficulty():
    difficulty = input("Select Difficulty. Type 'easy' or 'hard':\t")
    if difficulty == "easy":
        return 10
    else:
        return 5


def guess_the_number():
    num = random.randint(1, 100)
    win = False

    print(f"{logo}\nGuess the number between 1 and 100.")
    guesses_remaining = select_difficulty()
    print(f"You have {guesses_remaining} tries.")

    while guesses_remaining > 0 and not win:
        guess = int(input("Guess a number:\t"))
        if guess == num:
            print(f"Well Done!  The number was {num}")
            win = True
        elif guesses_remaining == 0 and not win:
            print(f"Out of guesses.  The number was {num}")
        elif guess > num:
            guesses_remaining -= 1
            print(f"Lower.\nYou have {guesses_remaining} more guesses")
        else:
            guesses_remaining -= 1
            print(f"Higher.\nYou have {guesses_remaining} more guesses")

    if input("Play Again? [Y/n] ").lower() == "n":
        exit()
    else:
        os.system("clear")
        guess_the_number()


guess_the_number()
