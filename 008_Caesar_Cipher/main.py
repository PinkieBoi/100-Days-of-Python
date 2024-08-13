import string

alphabet = string.ascii_lowercase * 2
message = input("Message to encrypt / decrypt:\n")
key = int(input("Encryption key:\n"))
mode = int(input("Enter 1 to encrypt or 2 to decrypt\n"))


def cipher(message, key, mode):
    output = ""
    for letter in message:
        if letter == " ":
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


cipher(message, key, mode)