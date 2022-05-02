"""TIC TAC TOE
Program that will simulate the game tic tac toe

Conditions: 
    X always goes first
    User always goes first
    Each number from 1-9 will represent the position on the grid"""

import random

#Variables
board = [' ' for x in range(10)] #Create a blank board

def insertBoard(letter, position):
    #Function that will insert x or o in the position chosen
    board[position] = letter

def freeSpace(position):
    #Function that checks if a space in the board is empty
    #Return true if a space is found otherwise return false
    return board[position] == ' '

def winner(position, letter):
    #Function that will determine which letter won based on the board.
    return ((board[7] == letter and board[8] == letter) and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def playerTurn():
    run = True #Loop condition that will continue until we get an invalid move

    while run:
        move = input('Select a position to place \'X\' (1-9)')
        try:
            if move > 0 and move < 10: #Range 1-9
                if freeSpace(move):
                    #Check if chosen position is a free spot
                    run = False
                    insertBoard('X', move)
                else:
                    print('This space has already been filled.')
            else:
                print('Invalid range. Please pick a number between 1 to 9')
        except:
            print('Please pick a number!')

def selectRandom(list):
    length = len(list) #Get the length of the list of numbers to chose
    randomNum = random.rangrange(0, length) #Pick a random number in the list 
    return list[randomNum]

def compareMove():
    currentMoves = [x for x, letter, in enumerate(board) if letter == ' ' and x !=0] #List of available moves
    move = 0

    #Check for possible winning moves to take or block opponents winning move
    for letter in ['O', 'X']:
        for i in possibleMoves:
            copyBoard = board[:]
            copyBoard[i] = letter
            if winner(board, letter):
                move = i
                return move

    #Take the corners
    corners = []
    for i in currentMoves:
        if i in [1,3,7,9]:
            corners.append(i)
    
    if len(corner) > 0:
        move = selectRandom(corners)
        return move

    #Take the centre
    if 5 in currentMoves:
        move = 5
        return move

    #Take edges
    edges = []
    for i in currentMoves:
        if i in [2,4,6,8]:
        edges.append(i)
    
    if len(edges) > 0:
        move = selectRandom(edges)

    return move

def boardFull(board):
    #Function that determines if there are no more spaces on the board
    if board.count(' ') > 1: #Will always have one blank spot in the board.
        return False
    else:
        return True

def printBoard(board):
    #Function that will display the board to the console
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def main():
    #Main game loop
    print('TIC TAC TOE\n')

    #Print the current empty board
    printBoard(board)

    #Loop through the game until the board is either full or someone wins the game
    while not(boardFull(board)):
        if not(winner(board, 'O')):
            playerTurn()
            printBoard(board)
        else:
            print('O\'s wins the round!')
            break

    if not(winner(board, 'X')):
        move = compareMove()
        if move == 0:
            print('Game is a Tie! There are no more turns.')
        else:
            insertBoard('O', move)
            print('Player 2 placed an \'O\' in position', move, ':')
            printBoard(board)

    else:
        print('\X\'s win. Good Job!')
        break

    if boardFull(board):
        print('Game is a Tie! There are no more turns.')


#Opening prompt for users to play the game and start
while True:
    answer = input('Do you want to play? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        #Answer is N
        break