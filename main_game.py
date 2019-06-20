#!/usr/bin/env python

from src.live import load_game, welcome
from src.utils import screen_cleaner

__author__ = 'khalilj'
__creation_date__ = '04/01/2019'


if __name__ == '__main__':
    try:
        screen_cleaner()
        print(welcome("Guy"))
        load_game()
    except KeyboardInterrupt as e:
        print("\nBye Bye")
    except Exception as e:
        print(e)
