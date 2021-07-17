"""Create a "Code" Generator that takes text as input
and replaces each letter with another letter,
and outputs the "encoded" message.

For all projects at beginner level user input validation is not performed.
"""


from string import ascii_letters, digits, punctuation


def shift_in_group(char: str, shift: int) -> str:
    """Func to calculate shifted index of char"""
    group = ascii_letters + digits + punctuation
    if char in group:
        max_index = len(group)
        char_index = group.index(char)
        new_index = char_index + shift
        #  That check provide availability to enter negative and
        #  bigger that total count of encoded chars, values
        if abs(new_index) >= max_index:
            new_index = (new_index % max_index)
        return group[new_index]
    else:
        return char


def encode_with_shift(message: str, shift: int) -> str:
    """Encode string via shifting index of char"""
    return ''.join([shift_in_group(char, shift) for char in message])


if __name__ == '__main__':
    while True:
        user_input = input('Enter phrase to encode: ')
        if user_input == '':
            break
        encode_shift = int(input('Enter shift value: '))
        encoded_msg = encode_with_shift(user_input, encode_shift)
        print(encoded_msg)
