from art_cipher import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '=', '_', '+', '/', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '?']

print(logo)


def caeser(original_text, shift_amt, dir):
    modified_text = ""
    if dir == "decode":
        shift_amt *= -1
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amt
            new_char = alphabet[new_position]
            modified_text += new_char
        elif char in numbers:
            position = numbers.index(char)
            new_position = position + shift_amt
            new_num = numbers[new_position]
            modified_text += new_num
        elif char in symbols:
            position = symbols.index(char)
            new_position = position + shift_amt
            new_sym = symbols[new_position]
            modified_text += new_sym
        else:
            modified_text += char
    print(f"The {dir}d text is {modified_text}")


should_end = False
while not should_end:
    direction = input(
        "Type 'encode' to encrypt, or 'decode; to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(original_text=text, shift_amt=shift, dir=direction)

    restart = input(
        "Want to go again? Type 'yes' or else type type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("See you again!")

# def encrypt(plain_text, shift_amt):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the ciphered text is {cipher_text}")


# def decrypt(plain_text2, shift_number2):
#     decipher_text = ""
#     for letter in plain_text2:
#         position = alphabet.index(letter)
#         new_position = position - shift_number2
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f"The deciphered text is {decipher_text} ")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amt=shift)
# elif direction == "decode":
#     decrypt(plain_text2=text, shift_number2=shift)
