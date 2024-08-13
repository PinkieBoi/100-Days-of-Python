# Check answer
# Replace correct blanks with guesses
# Check if player has won
# Track player Lives
import os
import lives
from wonderwords import RandomWord

# Generate Random Word
r = RandomWord()
word = list(r.word(word_min_length=4, word_max_length=8).lower())

lives_lost = 0
display = ""
for letter in word:
    display += "_"

while "_" in display and lives_lost < 6:
    print(lives.lost[lives_lost])
    print(display)
    guess = input("Make a Guess:\n\t").lower()
    if guess == "".join(word):
        # Win state
        print("You Win!!")
        display = guess
    elif guess in word:
        placeholder = ""
        for letter in word:
            if letter == guess:
                placeholder += letter
            elif letter in display:
                placeholder += letter
            else:
                placeholder += "_"
        display = placeholder
    else:
        # Wrong answer
        print("wrong")
        lives_lost += 1
    os.system("clear")
if lives_lost == 6:
    print(f"{lives.lost[lives_lost]}\nYou Lose!\nWord:  {"".join(word)}")
