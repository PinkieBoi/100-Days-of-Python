import string

alphabet = string.ascii_lowercase * 2


def cipher():
    message = input("Message to encrypt / decrypt:\n")
    key = int(input("Encryption key:\n"))
    mode = int(input("Enter 1 to encrypt or 2 to decrypt\n"))
    output = ""
    for letter in message:
        if letter not in alphabet:
            output += letter
        elif mode == 1:
            i = alphabet.index(letter) + key
            output += alphabet[i]
        elif mode == 2:
            i = alphabet.index(letter) - key
            output += alphabet[i]
        else:
            print("Invalid mode")
    print(output)
    while input("Run again? [y/N]").lower() == "y":
        cipher()


cipher()
