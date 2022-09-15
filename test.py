import copy
import math


X = "X"
O = "O"
EMPTY = None
board = [[O, EMPTY, EMPTY],
            [X, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def main():
    # print('actions:', actions(board))
    # print('result:', result(board, action))
    move = minimax(board)
    # print(move)
    # board = result(board, move)
    # print(board)


def player(board):
    num_x = 0
    num_o = 0
    for row in board:
        num_x += row.count(X)
        num_o += row.count(O)
    if num_x > num_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    action_lst = []
    for row in board:
        j = 0
        for _ in row:
            if _ == EMPTY:
                action_lst.append((i, j))
            j += 1
        i += 1

    return action_lst


def result(board, action):
    i, j = action
    new_board = copy.deepcopy(board)
    if board[i][j] == EMPTY:
        new_board[i][j] = player(board)
    else:
        raise Exception('wrong move')
    return new_board


def winner(board):
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
        diagonal2.append(board[i][2-i])
    if len(set(diagonal1)) == 1:
        return diagonal1[0]
    if len(set(diagonal2)) == 1:
        return diagonal2[0]


def terminal(board):
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    # while not terminal(board):

    # for action in actions(board):
    #     child_board = result(board, action)

    if player(board) == X:
        action = max_value(board)[1]
        # board = result(board, action)

    if player(board) == O:
        action = min_value(board)[1]
        # board = result(board, action)
    print(action)
    return action
    # print(board)


# def results(board, actions):
#     re_lst = []
#     for action in actions:
#         re_lst.append(utility(result(board, action)))
#     return re_lst


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    optimal_action = None
    for action in actions(board):
        # re_lst = []
        # child_board = result(board, action)
        # print('max child_board:', child_board)
        # print('child_board:', child_board)
        # print('child actions:', actions(child_board))
        # for child_action in actions(child_board):
        #     re_lst.append(utility(result(child_board, child_action)))
        # print(re_lst, max(re_lst))

        if v < min_value(result(board, action))[0]:
            v = min_value(result(board, action))[0]
            optimal_action = action
    return v, optimal_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    optimal_action = None
    for action in actions(board):
        # re_lst = []
        # child_board = result(board, action)
        # print('min child_board:', child_board)
        # print('child actions:', actions(child_board))
        # child_action = max_value(child_board)
        # for child_action in actions(child_board):
        #     re_lst.append(utility(result(child_board, child_action)))
        # print(re_lst, max(re_lst))

        if v > max_value(result(board, action))[0]:
            v = max_value(result(board, action))[0]
            optimal_action = action
    return v, optimal_action


if __name__ == '__main__':
    main()