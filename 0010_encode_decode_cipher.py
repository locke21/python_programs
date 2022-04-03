import os
clear = lambda: os.system('cls')

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def choice(direction, text, shift):
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decode(text, shift)
    elif direction == 'quit':
        quit()
    else:
        print('Invalid Choice, please choose again. ''\n')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit:\n").lower()
        choice(direction, text, shift)


def main_menu():
    clear()
    while True:
        shift = input("Select a shift number:\n")
        try:
            shift = int(shift)
            break
        except ValueError:
            print("Invalid number.")
    text = input("Type your message:\n").lower()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit:\n").lower()
    choice(direction, text, shift)


def encrypt(text, shift):
    encoded = ""
    for letter in text:
        if letter not in alphabet:
            encoded += letter
        else:
            orig_letter = alphabet.index(letter)
            shifted_letter = orig_letter + shift
            if shifted_letter >= 25:
                shifted_letter = shifted_letter - 26
                encoded += alphabet[shifted_letter]
            else:
                encoded += alphabet[shifted_letter]
    clear()
    print(f'You entered "{text}", the key number was {shift}.')
    print(f'The encoded text is "{encoded.upper()}".')
    input('\n''Press Enter to return to main menu.')
    main_menu()


def decode(text, shift):
    decoded = ""
    for letter in text:
        if letter not in alphabet:
            decoded += letter
        else:
            orig_letter = alphabet.index(letter)
            shifted_letter = orig_letter - shift
            if shifted_letter <= 0:
                shifted_letter = shifted_letter + 26
                decoded += alphabet[shifted_letter]
            else:
                decoded += alphabet[shifted_letter]
    clear()
    print(f'You entered "{text}", the key number was {shift}.')
    print(f'The decoded text is "{decoded.upper()}".')
    input('\n''Press Enter to return to main menu.')
    main_menu()


main_menu()
