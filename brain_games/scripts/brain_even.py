#!/usr/bin/env python

import brain_games.cli
import random


TRIES = 3
MIN_GAME_VAL = 1
MAX_GAME_VAL = 10000


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_correct_answer(value):
    if value % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game():
    game_value = random.randint(MIN_GAME_VAL, MAX_GAME_VAL)
    correct_answer = get_correct_answer(game_value)
    
    print(f'Question: {game_value}')
    answer = brain_games.cli.get_user_answer()

    correct = correct_answer == answer
    if correct:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    return correct


def play():
    print_rules()
    username = brain_games.cli.get_username()

    for i in range(0, TRIES):
        if not game():
            print(f"Let's try again, {username}!")
            break
    else:
        print(f"Congratulations, {username}!")
    

def main():
    brain_games.cli.welcome_user()
    play()


if __name__ == '__main__':
    main()
