""" Write a Sorting Method.
Given a list, can you write some code
that sorts it alphabetically, or numerically?
Yes, Python has this functionality built-in,
but see if you can do it without using sort()!

Time for sorting 1000 strings in list = 0.8081321716308594
Time for sorting 10000 strings in list = 97.70944690704346 :D
"""
from string import ascii_lowercase


unsorted_list = [
    'aa', 'ba', 'ca',
    'ab', 'bb', 'cb',
    'ac', 'bc', 'abjjjc']


def alphabet_sort(list_: list) -> list:
    """Bubble sorting"""
    max_index = len(list_) - 1
    finish_flag = False

    while not finish_flag:
        changes_count = 0

        for i in range(max_index):
            current_elem = list_[i]
            next_elem = list_[i + 1]
            for j, char in enumerate(current_elem):
                cur_char = char.lower()
                next_char = next_elem[j].lower()

                cur_char_index = ascii_lowercase.index(cur_char)
                nex_char_index = ascii_lowercase.index(next_char)

                if cur_char_index == nex_char_index:
                    continue
                if cur_char_index < nex_char_index:
                    break
                else:
                    list_[i + 1] = current_elem
                    list_[i] = next_elem
                    changes_count += 1

        if changes_count == 0:
            break
    return list_
