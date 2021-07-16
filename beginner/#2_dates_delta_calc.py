""" Build a 'countdown calculator.'
Write some code that can take two dates as input,
and calculate the amount of time between them.
This will be a great way to familiarize yourself
with Python's datetime module.

For all projects at beginner level user input validation is not performed.
"""

import datetime


def convert_input_to_date(user_input_date: str) -> datetime.date:
    """Parsing and hoping that user entered data according to the format"""
    user_date = [*map(int, user_input_date.split('.'))]
    day, month, year = user_date
    return datetime.date(year, month, day)


def time_calc_1() -> datetime.timedelta:
    prompt = 'Enter {var} date in format DD.MM.YYYY: '
    first_date = input(prompt.format(var='late'))
    second_date = input(prompt.format(var='early'))
    first_date = convert_input_to_date(first_date)
    second_date = convert_input_to_date(second_date)
    return second_date - first_date
