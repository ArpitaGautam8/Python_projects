import random
from turtle import clearscreen
from hangman_art import stages,logo
from hangman_words import word_list

end_of_game = False
lives = 6


chosen_word = random.choice(word_list)
print(logo)
print(f'Shh, the chosen word is: {chosen_word}')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
        display += "_"


while not end_of_game:
    guess = input("Guess a letter:")

    clearscreen

    if guess in display:
        print("The letter is already guessed.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, thats wrong")
        lives -=1
        print(f"Letter not in word.")
    if lives == 0:
        end_of_game = True
        print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game =True
        print("You win")


    print(stages[lives])