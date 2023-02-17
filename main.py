import numpy as np

board = np.full([3, 3], fill_value="-")
columns = {"A": "1", "B": "2", "C": "3"}
moves = {"Player 1": "X", "Player 2": "O"}


def show_board():
    for x in range(len(board)):
        if x == 0:
            print(f"   {list(columns.keys())[0]}", f"  {list(columns.keys())[1]}", f"  {list(columns.keys())[2]}")
        for y in range(len(board[x])):
            if y == 0:
                print(x+1, end=" ")
            item = board[x][y] + " |"
            if y == 2:
                item = board[x][y]
            print(f" {item}", end="")
        print(end="\n")
        if x == 2:
            break
        print("  -----------", end="\n")


def get_position(list_position):
    user_column = int(columns[list_position[0]]) - 1
    user_row = int(list_position[1]) - 1
    return user_row, user_column


def swap_turn(current_turn):
    player_list = list(moves.keys())
    next_turn = player_list[abs(player_list.index(current_turn) - 1)]
    return next_turn


def check_winner(current_turn):
    num = len(board)
    for x in range(num):
        win = True
        for y in range(num):
            if board[x][y] != moves[current_turn]:
                win = False
                break
        if win:
            return win

    for x in range(num):
        win = True
        for y in range(num):
            if board[y][x] != moves[current_turn]:
                win = False
                break
        if win:
            return win

    win = True
    for x in range(num):
        if board[x][x] != moves[current_turn]:
            win = False
            break
    if win:
        return win

    win = True
    for x in range(num):
        if board[x][num - 1 - x] != moves[current_turn]:
            win = False
            break
    if win:
        return win

    return False


def check_draw():
    for x in board:
        for y in x:
            if y == "-":
                return False
    return True


is_playing = True
current_player = "Player 1"

while is_playing:
    user_input = list(input(f"{current_player}: Enter a position on board: ").upper())

    row, column = get_position(user_input)

    if board[row][column] != "-":
        print("Position selected. Please pick another spot")
        continue
    else:
        board[row][column] = moves[current_player]

    show_board()

    if check_draw():
        print("It's a draw")
        break

    if check_winner(current_player):
        print(f"{current_player} has won the game!")
        break

    current_player = swap_turn(current_player)
