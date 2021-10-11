import brain_games.cli


TRIES = 3


def check_answer(answer, correct_answer):
    correct = str(correct_answer) == str(answer)
    if correct:
        print('Correct!')
    else:
        print(
            "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, correct_answer
            )
        )
    return correct


def game(generator):
    data = generator()

    print('Question: {}'.format(data['task']))
    answer = brain_games.cli.get_user_answer()

    return check_answer(answer, data['correct_answer'])


def play(data):
    print(data['desc'])
    username = brain_games.cli.get_username()

    for i in range(0, TRIES):
        if not game(data['generator']):
            print(f"Let's try again, {username}!")
            break
    else:
        print(f"Congratulations, {username}!")
