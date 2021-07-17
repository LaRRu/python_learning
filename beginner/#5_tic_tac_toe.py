"""
Tic-Tac-Toe by Text.
Build a Tic-Tac-Toe game that's playable
like a text adventure. Can you make
it print a text-based representation
of the board after each move?

For all projects at beginner level user input validation is not performed.
"""
from subprocess import call

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

players = ('X', 'O')


def print_board():
    """Func to print the pretty game board"""
    line_names = ['a', 'b', 'c']
    header = '   1   2   3'
    sep = '  ---+---+---'
    line = '{line_name}  {mark_1} | {mark_2} | {mark_3} '

    print(header)
    for i in range(3):
        line_name = line_names[i]
        mark_1, mark_2, mark_3 = board[i]

        print(line.format(
            line_name=line_name, mark_1=mark_1,
            mark_2=mark_2, mark_3=mark_3
        ))
        if i != 2:
            print(sep)


def get_turn_coords(point):
    '''Converting gamer convenient input to game-code format'''
    x_coords = {'1': 0, '2': 1, '3': 2}
    y_coords = {'a': 0, 'b': 1, 'c': 2}
    x_point, y_point = point
    x_point = x_coords[x_point]
    y_point = y_coords[y_point]

    return x_point, y_point


def is_valid_turn(point):
    '''Simple validation that cell isn't filled'''
    x_point, y_point = get_turn_coords(point)
    return board[y_point][x_point] == ' '


def make_turn(player):
    '''Making player`s turn function, which call itself if validation failed'''
    player_point = input('Enter coords for your turn [digit letter]: ')
    if is_valid_turn(player_point):
        x_index, y_index = get_turn_coords(player_point)
        board[y_index][x_index] = player
        return
    make_turn(player)


def change_player():
    global player
    if player is None:
        player = 'X'
        return
    player = 'X' if player == 'O' else 'O'


def is_game_ended():
    '''Func that checks win conditions with two nested functions:
        - checks the sequence: is all marks same;
        - creates all possible sequences (rows, columns, diagonals);'''
    def is_all_same(seq):
        seq = [x for x in seq if x in players]
        return len(seq) == 3 and len(set(seq)) == 1

    def get_all_lines():
        rows = [row for row in board]
        columns = [
            [board[i][j] for i in range(3)]
            for j in range(3)
            ]
        diagonals = [
            [board[i][i] for i in range(3)],
            [board[i][2-i] for i in range(2, -1, -1)]
        ]
        return rows + columns + diagonals

    for seq in get_all_lines():
        if is_all_same(seq):
            return True
    return False


def start_new_game():
    '''Clears all game variables'''
    global board
    global player
    player = None
    board = [[' ' for i in range(3)] for i in range(3)]


def finish_game():
    print(f'{player} won!')
    answer = input('Start new game(y/n)? ')
    if answer == 'y':
        game_loop()
    else:
        exit()


def game_loop():
    '''Main loop, that call functions in right order'''
    start_new_game()
    while not is_game_ended():
        change_player()
        print(f'{player}`s turn!')
        print_board()
        make_turn(player)
        call('Clear')
    finish_game()


if __name__ == '__main__':
    game_loop()
