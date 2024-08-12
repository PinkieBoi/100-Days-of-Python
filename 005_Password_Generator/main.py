import string
import random

letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Password Generator.\nSetup:")
letters_l = int(input("Number of lower case letters:\n\t"))
letters_u = int(input("Number of upper case letters:\n\t"))
nums = int(input("Number of numbers:\n\t"))
symbols_n = int(input("Number of symbols:\n\t"))

new_password = []

for _ in range(letters_l):
    new_password.append(random.choice(letters))

for _ in range(letters_u):
    new_password.append(random.choice(letters).upper())

for _ in range(nums):
    new_password.append(random.choice(numbers))

for _ in range(symbols_n):
    new_password.append(random.choice(symbols))

password = "".join(random.sample(new_password, len(new_password)))

print(f"Your password is:\n\t{password}")
