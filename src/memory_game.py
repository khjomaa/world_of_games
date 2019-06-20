#!/usr/bin/env python

import random
from time import sleep

__author__ = 'khalilj'
__creation_date__ = '04/09/2019'


class MemoryGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.__random_numbers = []

    def __generate_sequence(self):
        for i in range(self.difficulty):
            self.__random_numbers.append(random.randint(1, 101))

    def __get_list_from_user(self):
        user_numbers = []
        print(f'Try to guess the {self.difficulty} numbers:\r')

        for i in range(self.difficulty):
            while True:
                user_input = input()
                if not user_input or not user_input.isdigit() or int(user_input) < 1:
                    print(f'Invalid option! Please try again...\n')
                else:
                    break
            user_numbers.append(int(user_input))

        return user_numbers

    def __is_list_equal(self):
        return self.__random_numbers == self.__get_list_from_user()

    def play(self):
        self.__generate_sequence()
        print(self.__random_numbers, end='\r')
        sleep(0.7)
        print('*' * 25)

        if self.__is_list_equal():
            return True
        return False


if __name__ == '__main__':
    pass

    # TODO: For testing this class
    # game = MemoryGame(2)
    # print(game.play())
