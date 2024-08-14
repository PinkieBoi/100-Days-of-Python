import os
import time
from art import gavel

items = {"Laptop": ["", 0], "Tablet": ["", 0], "Phone": ["", 0]}


def place_bid(item):
    name = input("Bidder Name:\n").capitalize()
    bid_amount = round(float(input("Bid Value:\n$")), 2)
    if bid_amount > items[item][1]:
        items[item][0] = name
        items[item][1] = bid_amount
    print("\nBID ACCEPTED")
    time.sleep(3)
    os.system("clear")
    continue_bidding()


def display_items():
    print(f"{gavel}\nItems Available")
    for key in items:
        print(key)
    bid = input("\nWhich item would you like to bid on:\n").capitalize()
    place_bid(bid)


def winning_bids():
    for key in items:
        print(f"Winning bid for the {key}:\n\t{items[key][0]} with a bid of ${items[key][1]}")


def continue_bidding():
    more_bids = input("Any more bids?\n").lower()
    os.system("clear")
    if more_bids == "yes" or more_bids == "y":
        display_items()
    else:
        winning_bids()


display_items()
