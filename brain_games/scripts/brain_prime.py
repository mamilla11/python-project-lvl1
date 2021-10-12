#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.game import play
from brain_games.games.prime import init_game


def main():
    welcome_user()
    play(init_game())


if __name__ == '__main__':
    main()
