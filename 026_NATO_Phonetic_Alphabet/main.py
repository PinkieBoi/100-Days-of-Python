import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letter_list = data["letter"].tolist()

# spelling = [data.code[data.letter == letter].item() if letter in letter_list else letter for letter in message]

alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

message = input("Enter a word: ").upper()
spelling = [alpha_dict[letter] for letter in message]

print(spelling)
