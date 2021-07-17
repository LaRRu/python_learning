'''
Build a number guessing game.
Think of this as a bit like a text adventure,
but with numbers. How far can you take it?

For all projects at beginner level user input validation is not performed.
'''

from random import choice

max_num_prompt = 'Enter max number which will be used in game: '
game_start_prompt = 'Try to guess a num in range 0-{num}'
colors = {
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'END': '\033[0m',
    }


def create_random_num(max_num: int) -> int:
    return choice(range(max_num+1))


def check_user_input(user_num: int, guessing_num: int) -> str:
    if guessing_num == user_num:
        return 'equal!'
    elif guessing_num < user_num:
        return 'smaller'
    else:
        return 'greater'


def colored_print(msg: str, color: str) -> str:
    print(f"{colors[color]}{msg}{colors['END']}")


def mainloop(max_attempt_count: int):
    is_guessed = False

    user_guessing_range = int(input(max_num_prompt))
    guessing_num = create_random_num(user_guessing_range)
    colored_print(game_start_prompt.format(num=user_guessing_range), 'GREEN')

    while not is_guessed:
        colored_print(f'\nAttempts left: {max_attempt_count}', 'YELLOW')
        user_input = int(input('Enter your number: '))
        result = check_user_input(user_input, guessing_num)

        is_guessed = user_input == guessing_num
        colored_print(f'Guessed num is {result}', 'YELLOW')

        max_attempt_count -= 1
        if max_attempt_count == 0:
            colored_print('\nAttempt failed! You lost.', 'RED')
            break


if __name__ == '__main__':
    mainloop(max_attempt_count=10)
