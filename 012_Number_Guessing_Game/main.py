import os
import random


def select_difficulty():
    difficulty = input("Select Difficulty. Type 'easy' or 'hard':\t")
    if difficulty == "easy":
        return 10
    else:
        return 5


def guess_the_number():
    num = random.randint(0, 100)
    guesses_remaining = select_difficulty()
    win = False

    while guesses_remaining > 0 and win == False:
        guess = int(input("Guess a number:\t"))
        if guess == num:
            print(f"Well Done!  The number was {num}")
            win = True
        elif guesses_remaining == 0 and win == False:
            print(f"Out of guesses.  The number was {num}")
        elif guess > num:
            guesses_remaining -= 1
            print("Lower.")
        else:
            print("Higher.")
            guesses_remaining -= 1

    if input("Play Again? [Y/n] ").lower() == "n":
        exit()
    else:
        os.system("clear")
        guess_the_number()


guess_the_number()

