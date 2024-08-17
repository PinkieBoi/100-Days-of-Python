import os
import random
from art import logo

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
dealer_cards = []
player_cards = []


def deal_cards(player, num_cards):
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
    if score > 21 and "A" in cards:
        score -= 10
    return score


def gameplay():
    print(logo)
    if input("Play Blackjack? [Y/n] ").lower() == "n":
        exit()
    else:
        deal_cards(dealer_cards, 2)
        deal_cards(player_cards, 2)
        print(f"Your Cards: {player_cards}\tCurrent Score: {check_score(player_cards)}"
              f"\n\tComputer's first card: {dealer_cards[0]}")
        while check_score(player_cards) <= 21 and input("Enter 'H' to hit or 'S' to stand:  ").lower() == "h":
            os.system("clear")
            deal_cards(player_cards, 1)
            print(logo)
            print(f"Your Cards: {player_cards}\tCurrent Score: {check_score(player_cards)}"
                  f"\n\tComputer's first card: {dealer_cards[0]}")
        while check_score(dealer_cards) <= 17:
            deal_cards(dealer_cards, 1)
        os.system("clear")
        print(logo)
        print(f"Your Cards: {player_cards}\tYour Score: {check_score(player_cards)}\n"
              f"Computer Score:\t{check_score(dealer_cards)}")
        if check_score(player_cards) <= 21 and check_score(player_cards):
            print("You Win!")
        else:
            print("You Lose!")


gameplay()
