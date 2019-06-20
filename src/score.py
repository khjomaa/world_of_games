#!/usr/bin/env python

import os
from src.utils import SCORES_FILE_NAME, BAD_RETURN_CODE

__author__ = 'khalilj'
__creation_date__ = '05/13/2019'


def __get_current_score():
    exists = os.path.isfile(SCORES_FILE_NAME)

    if exists:
        with open(SCORES_FILE_NAME, 'r') as f:
            return f.read()
    else:
        return BAD_RETURN_CODE


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    current_score = int(__get_current_score())

    if current_score == BAD_RETURN_CODE:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(points_of_winning))
    else:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(points_of_winning + current_score))
