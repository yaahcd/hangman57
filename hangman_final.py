import random


class Hangman():
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        lowercase_guess = guess.lower()

        if lowercase_guess in self.word:
            print(f"Good guess! {lowercase_guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == lowercase_guess:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
        else:
            print(f"Sorry, {lowercase_guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} attempts left.")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        print(f"Guess  the word: {self.word_guessed}")

        while True:
            guess = input("Please enter a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break


def play_game(word_list):
    '''
    Starts the game with the word_list that has been passed as an argument.
    Keeps track of the games' state by checking two things:
    1. If the player has lives left to keep guessing
    2. If the player has guessed the word
    If none of the above is true, it calls the class' ask_for_input method.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break     
        elif game.num_letters > 0:
            game.ask_for_input()     
        else:
            print(f"Congratulations. You Won the game! The word was {game.word}.")
            break


if __name__ == "__main__":
    word_list = ["cherry", "blueberry", "mango", "papaya", "kiwi"]
    play_game(word_list)


