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
    Xcount=0
    Ocount=0
    for rows in board:
        for columns in rows:
            if columns ==X:
                Xcount += 1
            elif columns ==O:
                Ocount += 1
    if Xcount <= Ocount:
        return (X)
    else:
        return (O)

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    valid_moves = set()

    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                valid_moves.add((x,y))

    return (valid_moves)

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy=copy.deepcopy(board)
    if board_copy[action[0]][action[1]] != EMPTY:
        raise Exception("Move must be in empty square")
    else:
        board_copy[action[0]][action[1]] = player(board)
    return (board_copy)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        if (board[x][0]==board[x][1]==board[x][2]) and (board[x][0]!=EMPTY):
            return (board[x][0])
        if (board[0][x]==board[1][x]==board[2][x]) and (board[0][x]!=EMPTY):
            return(board[0][x])
    if ((board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0]))and(board[1][1]!=EMPTY):
        return (board[1][1])

    return (None)

    #done

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return (True)
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return(False)
    return(True)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        Utility=1
    elif winner(board)==O:
        Utility=-1
    else:
        Utility=0
    return (Utility)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return (None)
    if player(board) == X:
        score = -math.inf
        best_action = None
        for action in actions(board):
            min_val = MIN_POINTS(result(board, action))
            if min_val > score:
                score = min_val
                best_action = action
        return (best_action)
    elif player(board) ==O:
        score = math.inf
        best_action = None
        for action in actions(board):
            max_val = MAX_POINTS(result(board, action))
            if max_val<score:
                score = max_val
                best_action = action
        return (best_action)

def MIN_POINTS(board):
    if terminal(board):
        return utility(board)

    num=math.inf
    
    for action in actions(board):
        num=min(num,MAX_POINTS(result(board,action)))

    return num

def MAX_POINTS(board):
    if terminal(board):
        return utility(board)
    num = -math.inf
    for action in actions(board):
        num=max(num,MIN_POINTS(result(board,action)))

    return num
