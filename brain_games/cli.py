import prompt


username = ''


def welcome_user():
    global username
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')


def get_username():
    return username


def get_user_answer():
    return prompt.string('Your answer: ')
