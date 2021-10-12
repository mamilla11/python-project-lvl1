from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_GAME_VAL = 1
MAX_GAME_VAL = 100


def get_correct_answer(value):
    dividers = []

    for i in range(1, value):
        if value % i == 0:
            dividers.append(i)

    if len(dividers) == 2:
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
