#!/usr/bin/env python

from flask import Flask, render_template
from utils import SCORES_FILE_NAME

__author__ = 'khalilj'
__creation_date__ = '05/13/2019'

app = Flask(__name__)


def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        return f'{e.args[1]}: {e.filename}\n'


@app.route('/')
def index():
    return render_template('home.html', output=score_server())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
