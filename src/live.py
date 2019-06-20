#!/usr/bin/env python

from src.guess_game import GuessGame
from src.memory_game import MemoryGame
from src.currency_roulette_game import CurrencyRouletteGame
from src.score import add_score

__author__ = 'khalilj'
__creation_date__ = '04/01/2019'


def welcome(name):
    return f'''
Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play
'''


def load_game():
    res = False
    while True:
        game = input('''Please choose a game to play:
\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
\t2. Guess Game - guess a number and see if you chose like the computer
\t3. Currency Roulette - try and guess the value of a random amount of USD in ILs\n''')
        if not game or not game.isdigit() or int(game) < 1 or int(game) > 3:
            print(f'Invalid option! Please try again...\n')
        else:
            break

    while True:
        difficultly = input('Please choose game difficulty from 1 to 5:\n')
        if not difficultly or not difficultly.isdigit() or int(difficultly) < 1 or int(difficultly) > 5:
            print(f'Invalid option! Please try again...\n')
        else:
            break

    if int(game) == 1:
        memory_game = MemoryGame(int(difficultly))
        res = memory_game.play()
    elif int(game) == 2:
        guess_game = GuessGame(int(difficultly))
        res = guess_game.play()
    elif int(game) == 3:
        currency_game = CurrencyRouletteGame(int(difficultly))
        res = currency_game.play()

    if res:
        add_score(int(difficultly))
        print('\nYou won!')
    else:
        print('\nYou lose. Try again!')

