import os
import random

class Hangman():
    def __init__(self):
        self.word = self.pick_random_word()
        self.word = self.word.upper()
        self.hidden_word = ["-" for character in self.word]
        self.word_length = len(self.word)
        self.used_letters = []
        self.running = True
        self.lives = 10
        self.finished = False

        while self.running == True:
            self.handle_game()

    def pick_random_word(self):
        # Replace with the correct path
        filename = ".../Hangman/GermanWords/Words.txt"
        with open(filename, encoding="utf8") as file:
            content = file.readlines()

        content = [x.strip() for x in content]

        return (content[random.randrange(0, len(content))])

    def get_input(self):
        self.guess = input("Take a guess: \t")
        self.guess = self.guess.upper()
        return str(self.guess)

    def check_if_in_word(self, input):
        same = 0
        for i in range(len(self.word)):
            if self.word[i] == input and self.hidden_word[i] != input:
                self.update_output(i, input)
                same += 1
        return(same)

    def judge_answer(self, input):
        if len(input) == 0 or len(input) > 1:
            return True
        for character in self.used_letters:
            if character == input:
                return True
        return False

    def add_to_used(self, input):
        if not self.judge_answer(input):
            self.used_letters.append(input)


    def draw_word(self, won):
        os.system("cls")
        output_word = " ".join(self.hidden_word)
        output_letters = " ".join(self.used_letters)
        print(output_word)
        print("\nUsed:", output_letters)
        print("\nLives", self.lives, "\n\n")
        if self.finished == True:
            print(self.word, "\n")

    def update_output(self, place, letter):
        self.hidden_word[place] = letter

    def handle_game(self):
        if self.word_length > 0 and self.lives > 0:
            self.draw_word(self.finished)
            input = self.get_input()
            same_characters = self.check_if_in_word(input)
            self.word_length -= same_characters
            if same_characters <= 0 and not self.judge_answer(input):
                self.lives -=1

            self.add_to_used(input)
        else:
            self.finished = True
            self.draw_word(self.finished)
            self.running = False

Hangman()