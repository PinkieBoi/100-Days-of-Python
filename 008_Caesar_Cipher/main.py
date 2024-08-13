import string

alphabet = string.ascii_lowercase * 2


def cipher():
    message = input("Message to encrypt / decrypt:\n")
    mode = int(input("Enter 1 to encrypt or 2 to decrypt\n"))
    key = int(input("Enter your key\n"))
    output = []
    if mode == 1:
        for letter in message:
            if letter == " ":
                output.append(" ")
            else:
                out_index = alphabet.index(letter) + key
                output.append(alphabet[out_index])
    elif mode == 2:
       for letter in message:
            if letter == " ":
                output.append(" ")
            else:
                out_index = alphabet.index(letter) - key
                output.append(alphabet[out_index])
    else:
        print("Invalid Mode")
    
    print(f"Message:  {"".join(output)}")


cipher()
