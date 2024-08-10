import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

print("Let's play Rock Paper Scissors")
player_choice = int(input("Type 1 for Rock, 2 for Paper or 3 for Scissors\n")) - 1
print(player_choice)
computer_choice = random.choice(choices)

print(f"{choices[player_choice]}\nComputer chose:\n{computer_choice}")

if choices[player_choice] == computer_choice:
    print("Draw!")
elif player_choice == 0:
    if computer_choice == choices[2]:
        print("You Win!")
    else:
        print("You Lose!")
elif player_choice == 1:
    if computer_choice == choices[0]:
        print("You Win!")
    else:
        print("You Lose!")
elif player_choice == 2:
    if computer_choice == choices[1]:
        print("You Win!")
    else:
        print("You Lose!")
