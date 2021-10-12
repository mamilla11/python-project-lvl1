from random import randint


DESCRIPTION = 'What number is missing in the progression?'

MIN_START_VAL = 0
MAX_START_VAL = 50

MIN_STEP_VAL = 2
MAX_STEP_VAL = 10

SEQUENCE_LENGTH = 10


def get_game_data():
    game_values = [randint(MIN_START_VAL, MAX_START_VAL)]
    rand_step = randint(MIN_STEP_VAL, MAX_STEP_VAL)
    rand_secret = randint(0, SEQUENCE_LENGTH - 1)

    for i in range(1, SEQUENCE_LENGTH):
        game_values.append(game_values[i - 1] + rand_step)

    correct_answer = game_values[rand_secret]
    game_values[rand_secret] = '..'

    return {
        'task': ' '.join(map(str, game_values)),
        'correct_answer': correct_answer
    }


def init_game():
    return {
        'desc': DESCRIPTION,
        'generator': get_game_data
    }
