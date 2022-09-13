"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # count the number of X and O in the board
    num_x = 0
    num_o = 0
    for row in board:
        num_x += row.count(X)
        num_o += row.count(O)

    # determine the next player
    if num_x > num_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_lst = []
    i = 0
    for row in board:
        j = 0
        for _ in row:
            if _ == EMPTY:
                action_lst.append((i, j))
            j += 1
        i += 1
    return action_lst


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = copy.deepcopy(board)
    if board[i][j] == EMPTY:
        new_board[i][j] = player(board)
    else:
        raise Exception('wrong move')
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontally and vertically
    for i in range(3):
        column = []
        for row in board:
            if len(set(row)) == 1:
                return row[0]
            column.append(row[i])
        if len(set(column)) == 1:
            return column[0]

    # check diagonally
    diagonal1 = []
    diagonal2 = []
    for i in range(3):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][2 - i])
    if len(set(diagonal1)) == 1:
        return diagonal1[0]
    if len(set(diagonal2)) == 1:
        return diagonal2[0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        action = max_value(board)[1]

    if player(board) == O:
        action = min_value(board)[1]

    return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    optimal_action = None
    for action in actions(board):

        # if reach the maximum value, stop looping
        if min_value(result(board, action))[0] == 1:
            v = min_value(result(board, action))[0]
            optimal_action = action
            return v, optimal_action

        if v < min_value(result(board, action))[0]:
            v = min_value(result(board, action))[0]
            optimal_action = action

            # Alpha-beta pruning
            if v == 1:
                return v, optimal_action

    return v, optimal_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    optimal_action = None
    for action in actions(board):

        if v > max_value(result(board, action))[0]:
            v = max_value(result(board, action))[0]
            optimal_action = action

            # Alpha-beta pruning
            if v == -1:
                return v, optimal_action

    return v, optimal_action
