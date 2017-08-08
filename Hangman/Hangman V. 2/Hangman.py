import os
import random


class Hangman():
    def __init__(self):
        # Replace with the correct path
        self.filepath_words = ".../Hangman/GermanWords/Words.txt"
        self.word = self.pick_random_word()
        self.word = self.word.upper()
        self.hidden_word = ["-" for character in self.word]
        self.word_length = len(self.word)
        self.used_letters = []
        self.finished = False
        self.lives = 10
        self.guessed_right = 0

        while not self.finished:
            self.handle_game()

    def pick_random_word(self):
        with open(self.filepath_words, encoding="utf8") as file:
            content = file.readlines()

        content = [x.strip() for x in content]

        return (content[random.randrange(0, len(content))])

    def get_input(self):
        self.guess = input("Take a guess: \t")
        self.guess = self.guess.upper()
        return str(self.guess)

    def letter_in_word(self, input):
        for i in range(len(self.word)):
            if self.word[i] == input:
                return True
        return False

    def get_identical_letters(self, input):
        identical = []
        for i in range(len(self.word)):
            if self.word[i] == input:
                identical.append(i)
        return (identical)

    def valid_input(self, input):
        if len(input) == 0 or len(input) > 1:
            return False
        return True

    def already_used(self, input):
        for character in self.used_letters:
            if character == input:
                return True
        return False

    def add_to_used(self, input):
        if not self.already_used(input):
            self.used_letters.append(input)

    def draw_output(self):
        os.system("cls")
        output_word = " ".join(self.hidden_word)
        output_letters = " ".join(self.used_letters)
        print(output_word)
        print("\nUsed:", output_letters)
        print("\nLives", self.lives, "\n\n")

    def draw_solution(self):
        print(self.word)

    def update_output(self, place, letter):
        self.hidden_word[place] = letter

    def not_dead(self):
        if self.lives <= 0 or self.guessed_right == self.word_length:
            return False
        return True

    def handle_game(self):
        if self.not_dead():
            self.draw_output()
            guess = self.get_input()
            if self.valid_input(guess) and not self.already_used(guess) and not self.letter_in_word(guess):
                self.add_to_used(guess)
                self.lives -= 1
            elif self.valid_input(guess) and not self.already_used(guess) and self.letter_in_word(guess):
                self.add_to_used(guess)
                for letter_position in self.get_identical_letters(guess):
                    self.update_output(letter_position, guess)
                    self.guessed_right += 1
        if not self.not_dead():
            self.finished = True
            self.draw_output()
            self.draw_solution()

Hangman()