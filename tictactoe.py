"""
Tic Tac Toe Player
"""

import math
import random
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
    #raise NotImplementedError
    count=0
    for i in range(3):
        for j in range(3):
            if(board[i][j]!=EMPTY):
                count=count+1
    if(count%2==1):
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    possible_actions=set()
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY):
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    player_present=player(board)

    result_board = copy.deepcopy(board)

    if(player_present=='X'):
        result_board[action[0]][action[1]]=X
    else:
        result_board[action[0]][action[1]]=O
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    if board[0][0]==board[0][1]==board[0][2] and board[0][0]!=EMPTY:
        if board[0][0]==X:
            return X
        else:
            return O
    elif board[1][0]==board[1][1]==board[1][2] and board[1][0]!=EMPTY:
        if board[1][0]==X:
            return X
        else:
            return O
    elif board[2][0]==board[2][1]==board[2][2] and board[2][0]!=EMPTY:
        if board[2][0]==X:
            return X
        else:
            return O
    elif board[0][0]==board[1][0]==board[2][0] and board[0][0]!=EMPTY:
        if board[0][0]==X:
            return X
        else:
            return O
    elif board[0][1]==board[1][1]==board[2][1] and board[0][1]!=EMPTY:
        if board[0][1]==X:
            return X
        else:
            return O
    elif board[0][2]==board[1][2]==board[2][2] and board[0][2]!=EMPTY:
        if board[0][2]==X:
            return X
        else:
            return O
    elif board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        if board[0][0]==X:
            return X
        else:
            return O
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2]!=EMPTY:
        if board[0][2]==X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    if(winner(board)!=None or actions(board)==set()):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    if(winner(board)==X):
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def maxi(board):
    """
    Returns maximum cost form states possible
    """
    possible_actions=list(actions(board))
    cost=2
    maximum_cost=-2
    result_board=[]
    for action in possible_actions:
        result_board=result(board,action)
        if(terminal(result_board)):
            cost=utility(result_board)
            if(cost==1):
                return cost
        else:
            cost=mini(result_board)

        if maximum_cost<cost:
            maximum_cost=cost

    return maximum_cost

def mini(board):
    """
    Returns minimum cost form states possible
    """
    possible_actions=list(actions(board))

    cost=2
    minimum_cost=2
    result_board=[]
    for action in possible_actions:
        result_board=result(board,action)
        if(terminal(result_board)):
            cost=utility(result_board)
            if(cost==-1):
                return cost
        else:
            cost=maxi(result_board)

        if minimum_cost>cost:
            minimum_cost=cost


    return minimum_cost



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError

    if board == initial_state():
        return (random.randint(0, 2), random.randint(0, 2))

    possible_actions=list(actions(board))
    index=0
    cost=2
    maximum_cost=-2
    minimum_cost=2
    result_board=[]
    # if the user choises to play as X
    if(player(board)=='X'):
        for i, action in enumerate(possible_actions):
            result_board=result(board,action)

            if(terminal(result_board)):
                cost=utility(result_board)
                if(cost==1):
                    return action
            else:
                cost=mini(result_board)


            if maximum_cost<cost:
                maximum_cost=cost
                index=i
    # if the user choises to play as O
    else:
        for i, action in enumerate(possible_actions):
            result_board=result(board,action)
            if(terminal(result_board)):
                cost=utility(result_board)
                if(cost==-1):
                    return action
            else:
                cost=maxi(result_board)


            if minimum_cost>cost:
                minimum_cost=cost
                index=i
    return possible_actions[index]
