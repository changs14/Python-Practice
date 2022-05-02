""" SUDOKU SOLVER """
""" Using backtracking algorithm to solve the game Sudoku """

#Default board
from concurrent.futures.process import _threads_wakeups


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Backtracking algorithm
#1. Pick a random empty square
#2. Try all possible numbers 1-9
#3. Find a number that works
#4. Repeat
#5. Backtrack when a solution doesn't work

def print_board(board):
    #Print the sudoku board

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            #9 Squares in a row so check if i has reached end of row
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                #Print | for every three elements in a row
                print(" | ", end="")
                
            #Print values in the board
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def valid_board(board, number, position):
    #Check row, col, and square

    #Check row - loop through every column in the row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            #Ignore most recent position that was filled with a number
            return False

    #Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #Check square - determine which box we are in
    box_x = position[1] // 3 #Determine which box we are in in terms of x
    box_y = position[0] // 3 #Determine the row of the current box

    for i in range(box_y * 3, box_y*3+3):
        for j in range(box_x * 3, box_x*3+3):
            if board[i][j] == number and (i,j) != position:
                #Return false if current board index is the number that was just added 
                return False

    return True #All validity checks did not go through

def find_empty_square(board):
    #Find a square that is empty (represented by 0)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #return col and row index

    return None #Return none if there are no empty squares

def solve(board):
    #Solve the board with backtracking algorith.
    #Use recursion

    empty = find_empty_square(board)
    if not empty:
        #Return true if solution is found
        return True
    else:
        row, col = empty #Assign index of empty position

    for i in range(1,10):
        if valid_board(board, i, (row, col)):
            board[row][col] = i #Assign valid number into the square

            #Call solve on the new board with newly assigned value
            if solve(board):
                return True
            
            board[row][col] = 0 #Backtrack
    
    return False #Return false if loop through 1-9 and all numbers are invalid

print("\nUnsolved Board:\n***********************")
print_board(board)
solve(board)
print("\nSolved Board:\n***********************")
print_board(board)

