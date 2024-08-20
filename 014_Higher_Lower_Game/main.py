import os
import art
import game_data
from random import choice


def make_guess(account1, account2, wins):
    if wins > 0:
        print(f"Well done! Current score: {wins}")
    print(f"Compare A: {account1['name']} ({account1['description']}) from {account1['country']}"
          f"{art.vs}\nAgainst B: {account2['name']} ({account2['description']}) from {account2['country']}")
    guess = input("Who has more followers? Type A or B:\t")
    if guess == "a":
        return account1
    else:
        return account2


def check_win(guess, account1, account2):
    if float(account1["followers"]) > float(account2["followers"]):
        if guess == account1:
            return True
        else:
            return False
    else:
        if guess == account1:
            return False
        else:
            return True


def gameplay(wins):
    os.system("clear")
    print(f"{art.logo}")
    total_wins = wins
    data = game_data.data
    user_one = choice(data)
    user_two = choice(data)
    while user_one == user_two:
        user_two = choice(data)
    player_guess = make_guess(user_one, user_two, total_wins)
    if check_win(player_guess, user_one, user_two):
        total_wins += 1
        gameplay(total_wins)
    else:
        exit()


gameplay(0)
