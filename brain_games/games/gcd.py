from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_GAME_VAL = 1
MAX_GAME_VAL = 100


def get_correct_answer(value):
    if value % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_correct_answer(game_value1, game_value2):
    max_div = 1
    for i in range(2, min(game_value1, game_value2) + 1):
        if game_value1 % i == 0 and game_value2 % i == 0:
            max_div = i
    return max_div


def get_game_data():
    game_value1 = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    game_value2 = randint(MIN_GAME_VAL, MAX_GAME_VAL)

    correct_answer = get_correct_answer(game_value1, game_value2)

    return {
        'task': f'{game_value1} {game_value2}',
        'correct_answer': correct_answer
    }


def init_game():
    return {
        'desc': DESCRIPTION,
        'generator': get_game_data
    }
