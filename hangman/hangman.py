import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed

    while len(word_letters) > 0:
        # Show the letters used so far
        print('You have used these letters: ', ' '.join(used_letters))
        
        # Show the current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        # Get the user input
        user_letter = input("Guess the letter: ").upper()
        
        # If the letter is valid and hasn't been used yet
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! '{user_letter}' is in the word.")
            else:
                print(f"'The letter {user_letter}' is not in the word.")
        
        # If the letter has already been used
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
        # If the letter is not a valid character
        else:
            print("Invalid character. Please try again.")

    # When the user guesses the word
    print(f"Congratulations! You guessed the word: {word}")

hangman()