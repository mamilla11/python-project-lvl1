#!/usr/bin/env python

import brain_games.cli
from random import randint
from operator import mul, add, sub


TRIES = 3
MIN_GAME_VAL = 1
MAX_GAME_VAL = 200
GAME_OPERATORS = {'*': mul, '-': sub, '+': add}


def print_rules():
    print('What is the result of the expression?')


def check_answer(answer, correct_answer):
    correct = str(correct_answer) == str(answer)
    if correct:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    return correct


def get_correct_answer(game_value1, game_value2, game_op):
    return GAME_OPERATORS[game_op](game_value1, game_value2)


def game():
    game_value1 = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    game_value2 = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    game_op = list(GAME_OPERATORS.keys())[randint(0, len(GAME_OPERATORS) - 1)]

    correct_answer = get_correct_answer(game_value1, game_value2, game_op)

    print(f'Question: {game_value1} {game_op} {game_value2}')
    answer = brain_games.cli.get_user_answer()

    return check_answer(answer, correct_answer)


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
