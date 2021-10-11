from random import randint
from operator import mul, add, sub


DESCRIPTION = 'What is the result of the expression?'
GAME_OPERATORS = {'*': mul, '-': sub, '+': add}
MIN_GAME_VAL = 1
MAX_GAME_VAL = 100


def get_game_data():
    game_value1 = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    game_value2 = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    game_op = list(GAME_OPERATORS.keys())[randint(0, len(GAME_OPERATORS) - 1)]

    correct_answer = GAME_OPERATORS[game_op](game_value1, game_value2)

    return {
        'task': f'{game_value1} {game_op} {game_value2}',
        'correct_answer': correct_answer
    }


def init_game():
    return {
        'desc': DESCRIPTION,
        'generator': get_game_data
    }
