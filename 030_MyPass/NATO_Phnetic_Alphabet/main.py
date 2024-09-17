import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letter_list = data["letter"].tolist()

alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# spelling = [data.code[data.letter == letter].item() if letter in letter_list else letter for letter in message]


def phonetic_spelling():
    message = input("Enter a word: ").upper()
    try:
        spelling = [alpha_dict[letter] for letter in message]
    except KeyError:
        print("Only letters in the english alphabet, please.")
        phonetic_spelling()
    else:
        print(spelling)


phonetic_spelling()
