import itertools
import os
import numpy as np
import pandas as pd


def check_victory_condition(board, player):
    board = np.array(board)
    for i in range(4):
        row = board[(i * 4):(i * 4 + 4)]
        col = board[i::4]
        if np.sum(row) == 4*player or np.sum(col) == 4*player:
            return True
        if np.sum(board[[0, 4, 8]]) == 4*player or np.sum(board[[2, 4, 6]]) == 4*player:
            return True


def judge(board):
    # Check which is the current player
    if np.sum(board) == 0:
        player = 1
    else:
        player = -1
    # Check endgame
    for i in range(4):
        row = board[(i*4):(i:4+4)]
        col = board[i::4]
        if np.sum(row) == 3 or np.sum(col) == 3:
            return 1
        if np.sum(row) == -3 or np.sum(col) == -3:
            return -1
    # Check diag
    if np.sum(board[[0, 4, 8]]) == 3 or np.sum(board[[2, 4, 6]]) == 3:
        return 1
    if np.sum(board[[0, 4, 8]]) == -3 or np.sum(board[[2, 4, 6]]) == -3:
        return -1
    if 0 not in board:
        return 0
    # Recursive search
    results = []
    for i in range(len(board)):
        if board[i] == 0:
            next_board = np.array(board)
            next_board[i] = player
            result = judge(next_board)
            if player == result:
                return player
            results.append(result)
    if 0 in results:
        return 0
    else:
        return -player


if __name__ == "__main__":
    l = []
    for i in itertools.product((-1, 0, 1), repeat=9):
        if sum(i) >= 2 or sum(i) <= -1:
            continue
        if check_victory_condition(i, 1) and check_victory_condition(i, -1):
            print "Invalid Board:", i
            continue
        print("Board: {}".format(i))
        result = judge(np.array(i))
        print("Result: {}".format(result))
        l.append(list(i) + [result])

    col_names = [
        "Top-first", "Top-second", "Top-third","Top-fourth",
        "Middle1-first", "Middle1-second", "Middle1-third","Middle1-fourth",
        "Middle2-first", "Middle2-second", "Middle2-third","Middle2-fourth",
	"Bottom-first","Bottom-second","Bottom-third","Bottom-fourth",
        "result"
    ]
    df = pd.DataFrame(data=l, columns=col_names)
    df.to_csv(os.path.join("data", "tictactoe1.csv"), index=False)
