import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ["_"] * len(self.word)
        self.list_of_guesses = []


    def check_guess(self, guess):
        lowercase_guess = guess.lower()

        if lowercase_guess in self.word:
            print(f"Good guess! {lowercase_guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
        else:
            print(f"Sorry, {lowercase_guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} attempts left.")


    def ask_for_input(self):
        is_playing = True

        while is_playing:
            guess = input("Please enter a letter: ")

            if not guess.isalpha():
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
    num_lives = 5
    game = Hangman(word_list, num_lives)
    is_playing = True

    while is_playing:
        if game.num_lives == 0:
            print("You lost!")
            break     
        elif game.num_letters > 0:
            game.ask_for_input()     
        else:
            print(f"Congratulations. You Won the game! The word was {game.word}.")
            break

word_list = ["cherry", "blueberry", "mango", "papaya", "kiwi"]
play_game(word_list)
