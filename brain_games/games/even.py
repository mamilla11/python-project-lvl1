from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_GAME_VAL = 1
MAX_GAME_VAL = 100


def get_correct_answer(value):
    if value % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_game_data():
    game_value = randint(MIN_GAME_VAL, MAX_GAME_VAL)
    correct_answer = get_correct_answer(game_value)

    return {
        'task': game_value,
        'correct_answer': correct_answer
    }


def init_game():
    return {
        'desc': DESCRIPTION,
        'generator': get_game_data
    }
