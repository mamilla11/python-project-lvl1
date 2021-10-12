import brain_games.games.even as even


def test_get_correct_answer():
    assert even.get_correct_answer(2) == 'yes'
    assert even.get_correct_answer(3) == 'no'


def test_get_game_data():
    data = even.get_game_data()

    assert len(data) == 2
    assert type(data['task']) == int 
    assert type(data['correct_answer']) == str
    assert data['correct_answer'] == 'yes' or data['correct_answer'] == 'no'


def test_init_game():
    data = even.init_game()

    assert len(data) == 2
    assert type(data['desc']) == str
    assert callable(data['generator'])
