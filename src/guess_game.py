#!/usr/bin/env python

import random

__author__ = 'khalilj'
__creation_date__ = '04/09/2019'


class GuessGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.__secret_number = 0

    def __generate_number(self):
        self.__secret_number = random.randint(1, self.difficulty)

    def __get_guess_from_user(self):
        while True:
            user_input = input(f'Please guess a number between 1 to {self.difficulty}:\n')
            if not user_input or not user_input.isdigit() or int(user_input) < 1 or int(user_input) > self.difficulty:
                print(f'Invalid option! Please try again...\n')
            else:
                break
        return int(user_input)

    def __compare_results(self):
        return self.__secret_number == self.__get_guess_from_user()

    def play(self):
        self.__generate_number()

        if self.__compare_results():
            return True
        return False


if __name__ == '__main__':
    pass

    # TODO: For testing this class
    # game = GuessGame(5)
    # print(game.play())
