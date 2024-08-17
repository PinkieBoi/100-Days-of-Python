import os
import random
from art import logo
from time import sleep


def deal_cards(player, num_cards):
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    while num_cards > 0:
        player.append(random.choice(deck))
        num_cards -= 1


def check_score(cards):
    score = 0
    for n in cards:
        if n == "A":
            score += 11
        elif n in ["J", "Q", "K"]:
            score += 10
        else:
            score += n
    if score == 21 and len(cards) == 2:
        return 0
    if score > 21 and "A" in cards:
        score -= 10
    return score


def gameplay():
    computer_cards = []
    player_cards = []
    os.system("clear")
    if input(f"{logo}\nPlay Blackjack? [Y/n] ").lower() == "n":
        exit()
    else:
        deal_cards(computer_cards, 2)
        deal_cards(player_cards, 2)
        print(f"Your Cards: {player_cards}\tCurrent Score: {check_score(player_cards)}"
              f"\n\tComputer's first card: {computer_cards[0]}")
        if check_score(computer_cards) == 0:
            print("Blackjack.  Computer Wins!")
            gameplay()
        elif check_score(player_cards) == 0:
            print("Blackjack.  You Win!")
            gameplay()
        else:
            while check_score(player_cards) <= 21 and input("Enter 'H' to hit or 'S' to stand:  ").lower() == "h":
                os.system("clear")
                deal_cards(player_cards, 1)
                print(f"{logo}\nYour Cards: {player_cards}\tCurrent Score: {check_score(player_cards)}"
                      f"\n\tComputer's first card: {computer_cards[0]}")
            while check_score(computer_cards) <= 17:
                deal_cards(computer_cards, 1)
            os.system("clear")
            print(f"{logo}\nYour Cards: {player_cards}\tYour Score: {check_score(player_cards)}\n"
                  f"Computer Score:\t{check_score(computer_cards)}")
            if check_score(player_cards) <= 21 and check_score(player_cards):
                print("You Win!")
            else:
                print("You Lose!")
            sleep(3)
            gameplay()


gameplay()

