#!/usr/bin/env python

import platform
from subprocess import call

__author__ = 'khalilj'
__creation_date__ = '05/13/2019'

SCORES_FILE_NAME = 'src/scores.txt'
BAD_RETURN_CODE = -1


def screen_cleaner():
    command = "cls" if platform.system().lower() == "windows" else "clear"

    try:
        call(command, shell=True)
    except Exception as e:
        print(e)

