ascii_art = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"\"\"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
print(ascii_art + "\nWelcome to Treasure Island\nYour mission is to find the treasure.")

if input("You're at a cross road.  Where do you want to go?\n\tType 'left' or 'right'\n").lower() == "left":
    print("You've come to a lake.  There is an island in the middle of the lake.")
    if input("\tType 'wait' to wait for a boat.  Type 'swim' to swim across\n").lower() == "wait":
        print("You reach the island where you find a house with three doors.\n \
        One red, one yellow and one blue.")
        door = input("\tWhich color door do you open?\n").lower()
        if door == "red":
            print("You awake a slumbering dragon and die a fiery death.")
        elif door == "blue":
            print("As you walk down a dark hall you are ambushed by Kobalds who tear you limb from limb. \
                  \n\tGame Over!")
        elif door == "yellow":
            print("You find a chest overflowing with treasure.\n\tYou Win!")
        else:
            print("You hesitate too long and a trap door opens beneath your feet. \
            \nYou plummet to your death.\n\tGame Over!")
    else:
        print("You are dragged to your death by a giant sqiud.\n\tGame Over!")
else:
    print("You fall into a hole and die cold and alone.\n\tGame Over!")
