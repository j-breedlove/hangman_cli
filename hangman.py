import random

from hangman_art import stages, logo
from hangman_words import word_list


def choose_word(word_list):
    """
    Choose a random word from the provided list.

    Args:
    - word_list (list): A list of words to choose from.

    Returns:
    - str: A randomly chosen word.
    """
    return random.choice(word_list)


def display_hangman(lives):
    """
    Display the current state of the hangman based on the number of lives left.

    Args:
    - lives (int): The number of lives left.
    """
    print(stages[lives])


def play_game():
    """
    Main function to handle the flow of the Hangman game.
    """
    print(logo)
    chosen_word = choose_word(word_list)

    display = ["_"] * len(chosen_word)
    print(" ".join(display))

    lives = 6
    while "_" in display and lives > 0:
        guess = input("\nGuess a letter: ").lower()

        if guess in display:
            print(f"You have already guessed {guess}")

        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            display_hangman(lives)
            print(f"You have {lives} lives left")
            if lives == 0:
                print("You lose!")
                break

        print(" ".join(display))

    if "_" not in display:
        print("You win!")
    print(f"The word was {chosen_word}")


# Uncomment the next line to play the game
play_game()
