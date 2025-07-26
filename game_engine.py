import random
from word_bank import words
from hangman_visuals import display_hangman
from score_tracker import log_result, generate_score_chart
from utils import colored_text


def play_game():
    word, hint = random.choice(list(words.items()))
    word_letters = set(word)
    guessed_letters = set()
    attempts_left = 6

    print(colored_text("Welcome to Hangman!", "cyan"))
    print(f"Hint: {hint}")

    while len(word_letters) > 0 and attempts_left > 0:
        print(display_hangman(attempts_left))
        display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current Word:", ' '.join(display))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print(colored_text("You already guessed that.", "yellow"))
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            guessed_letters.add(guess)
            attempts_left -= 1
            print(colored_text("Wrong guess!", "red"))

    if attempts_left == 0:
        print(display_hangman(attempts_left))
        print(colored_text(f"You lost! The word was: {word}", "red"))
        log_result(word, "LOSE")
    else:
        print(colored_text(f"Congratulations! You guessed the word: {word}", "green"))
        log_result(word, "WIN")

    generate_score_chart()
