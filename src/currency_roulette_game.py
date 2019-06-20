#!/usr/bin/env python

import random
import requests

__author__ = 'khalilj'
__creation_date__ = '04/09/2019'

BASE_URL = 'https://api.exchangerate-api.com/v4/latest/USD'


class CurrencyRouletteGame:

    def __init__(self, difficulty, debug_mode=False):
        self.difficulty = difficulty
        self.debug_mode = debug_mode
        self.__random_number = random.randint(1, 101)

    def __get_usd_rate_in_ils(self):
        response = requests.get(BASE_URL)
        data = response.json()
        ils_rate = data['rates']['ILS']
        if self.debug_mode:
            print(f'1 USD = {round(ils_rate, 2)} ILS')
        return ils_rate

    def __get_money_interval(self):
        usd_rate = self.__get_usd_rate_in_ils()
        total_value = self.__random_number * usd_rate
        # For given difficulty d, and total value of money the interval will be: (t - (5 - d), t + (5 - d))
        return round(total_value - (5 - self.difficulty), 2), round(total_value + (5 - self.difficulty), 2)

    def __get_guess_from_user(self):
        while True:
            user_input = input(f'Please guess the value of {self.__random_number}$ in ILS:\n')
            if not user_input or isinstance(user_input, float):
                print(f'Invalid option! Please try again...\n')
            else:
                break
        return float(user_input)

    def play(self):
        lower, higher = self.__get_money_interval()
        if self.debug_mode:
            print(f'Lower value interval: {lower}, Higher money interval: {higher}')
        guessed_value = self.__get_guess_from_user()
        if lower <= guessed_value <= higher:
            return True
        return False


if __name__ == '__main__':
    pass

    # TODO: For testing this class ONLY
    # game = CurrencyRouletteGame(3, debug_mode=True)
    # print(game.play())
