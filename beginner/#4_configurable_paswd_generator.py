""" Build an Interactive Quiz.
Build a personality or recommendation quiz
that can asks users some questions,
stores their answers, and then perform some
kind of calculation to give the user a personalized
end result that's based on their answers.
-----
As I recognize, the main idea of this project is
to create a some interactive script, which would
ask a user some questions and return result depends
on users answers. Let's create a password generator.

For all projects at beginner level user input validation is not performed.
"""
from string import (
    ascii_letters, ascii_lowercase,
    ascii_uppercase, digits, punctuation
    )
from random import choices


symbols_dict = {
    1: ascii_lowercase,
    2: ascii_uppercase,
    3: ascii_letters,
    4: digits,
    5: punctuation,
    6: '',
}


def get_user_input():
    user_symbols = None
    pass_len = int(input('Enter required passwd length: '))

    print('Enter allowed symbols for password with spaces:\n\
            1 - lower case letters, 2 - upper case letters\n\
            3 - all letters, 4 - digits, 5 - punctuation\n\
            6 - user defined symbols \n')

    symbols_groups = input('>>> ')
    symbols_groups = {
        group: value
        for group, value in symbols_dict.items()
        if str(group) in symbols_groups
        }

    if 6 in symbols_groups.keys():
        user_symbols = input('Enter symbols: ')
        symbols_groups[6] = user_symbols

    return (pass_len, symbols_groups)


def generate_unuseful_passwd(passwd_len, symbols_groups):
    symbols = ''.join(symbols_groups.values())
    passwd = ''.join(choices(symbols, k=passwd_len))
    return passwd


if __name__ == '__main__':
    passwd = generate_unuseful_passwd(*get_user_input())
    print(passwd)
