# File: p1.py
# Author: Jake Natalizia
# Date: November 4th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Connect Four
# Collaboration: I did not collaborate with anyone.

import random

# CONSTANTS
P1_MARK = "x"
P2_MARK = "o"

# Gets board/game parameters
def gameSetup():
    # Gets row size
    rowSize = ""
    while rowSize == "":
        rowSize = int(input("Please enter your desired row size: "))
        # Input validation
        if rowSize < 5:
            print("Row size must be at least 5.")
            rowSize = ""

    # Get column size
    columnSize = ""
    while columnSize == "":
        columnSize = int(input("Please enter your desired column size: "))
        # Input validation
        if columnSize < 5:
            print("Column size must be at least 5.")
            columnSize = ""

    # Ask for game type
    print("-"*35)
    print("Do you want to play against the computer? Y/N")
    gameChoice = ""
    while gameChoice == "":
        # Player vs. Computer
        gameChoice = input("\tY for YES, N for NO: ")
        if gameChoice == "y":
            print("SELECTED: Player vs. Computer")
            onePlayer(rowSize, columnSize)
        # Player vs. Player
        elif gameChoice == "n":
            print("SELECTED: Player vs. Player")
            twoPlayers(rowSize, columnSize)
        else:
            print("Please enter a \"y\" or a \"n\".")
            gameChoice = ""

# For playing against the computer
def onePlayer(row,col):
    # Prints out board
    board = [["_"] * row for i in range(col)]
    totalMoves = row * col

    # Keeps track of which column to move up to
    columnCount = []
    for i in list(range(row)):
        columnCount.append(1)

    # Limits amount of turns to totalMoves (REPLACE WITH: WHILE != WIN CONDITION)
    for i in range(0, totalMoves - 1):
        # Player 1 goes when 1, Player 2 goes when 2
        turnCounter = 1

        # PLAYER ONE'S TURN
        while turnCounter == 1:
            updateBoard(board)

            # Input validation for column choice
            columnChoice = 0
            while columnChoice == 0 or columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                columnChoice = int(input("PLAYER 1'S TURN\n\tChoose a column (1 - " + str(row) +  "): "))
                if columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                    print("Invalid choice. Column is full or not in range.")

            # Decremented to easily reference list indexes
            columnChoice -= 1

            # If the player's selection is already marked, mark the row above it
            if board[col-(columnCount[columnChoice])][columnChoice] == P1_MARK or board[col-(columnCount[columnChoice])][columnChoice] == P2_MARK:
                columnCount[columnChoice] += 1
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                turnCounter += 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                turnCounter += 1
        
        # COMPUTER'S TURN
        while turnCounter == 2:
            updateBoard(board)

            # Input validation for column choice
            columnChoice = 0
            while columnChoice == 0 or columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                columnChoice = random.randrange(1,col)
                if columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                    columnChoice == 0
            print("COMPUTER CHOOSES COLUMN " + str(columnChoice))

            # Decremented to easily reference list indexes
            columnChoice -= 1

            # If the player's selection is already marked, mark the row above it
            if board[col-(columnCount[columnChoice])][columnChoice] == P1_MARK or board[col-(columnCount[columnChoice])][columnChoice] == P2_MARK:
                columnCount[columnChoice] += 1
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                turnCounter -= 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                turnCounter -= 1

# For two players playing each other
def twoPlayers(row,col):
    # Prints out board
    board = [["_"] * row for i in range(col)]
    totalMoves = row * col

    # Keeps track of which column to move up to
    columnCount = []
    for i in list(range(row)):
        columnCount.append(1)

    # Limits amount of turns to totalMoves (REPLACE WITH: WHILE != WIN CONDITION)
    for i in range(0, totalMoves - 1):
        # Player 1 goes when turnCounter is 1, Player 2 goes when turnCounter is 2
        turnCounter = 1

        # PLAYER ONE'S TURN
        while turnCounter == 1:
            updateBoard(board)
            checkEndGame(board,row,col,turnCounter)

            # Input validation for column choice
            columnChoice = 0
            while columnChoice == 0 or columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                columnChoice = int(input("PLAYER 1'S TURN\n\tChoose a column (1 - " + str(row) +  "): "))
                if columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                    print("Invalid choice. Column is full or not in range.")

            # Decremented to easily reference list indexes
            columnChoice -= 1

            # If the player's selection is already marked, mark the row above it
            if board[col-(columnCount[columnChoice])][columnChoice] == P1_MARK or board[col-(columnCount[columnChoice])][columnChoice] == P2_MARK:
                columnCount[columnChoice] += 1
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                turnCounter += 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                turnCounter += 1
        
        # PLAYER TWO'S TURN
        while turnCounter == 2:
            updateBoard(board)
            checkEndGame(board,row,col,turnCounter)

            # Input validation for column choice
            columnChoice = 0
            while columnChoice == 0 or columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                columnChoice = int(input("PLAYER 2'S TURN\n\tChoose a column (1 - " + str(row) +  "): "))
                if columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                    print("Invalid choice. Column is full or not in range.")

            # Decremented to easily reference list indexes
            columnChoice -= 1

            # If the player's selection is already marked, mark the row above it
            if board[col-(columnCount[columnChoice])][columnChoice] == P1_MARK or board[col-(columnCount[columnChoice])][columnChoice] == P2_MARK:
                columnCount[columnChoice] += 1
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                turnCounter -= 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                turnCounter -= 1

# Prints the board in its current state
def updateBoard(board):
    for element in board:
        for i in element:
            print(i, end=' ')
        print("")

def checkEndGame(board,row,col,turnCounter):
    a = 0

    # Horizontal win condition for player 1
    for row in board:
        # Used for iterating through different "blocks of four"
        b = a + 1
        c = b + 1
        d = c + 1
        if d <= col:
            if row[a] == P1_MARK and row[b] == P1_MARK and row[c] == P1_MARK and row[d] == P1_MARK:
                playerOneWin()
            a += 1
        # When d exceeds the range of "row"
        elif d > col:
            a = 0
        
# Win condition for player 1
def playerOneWin():
    print("Player 1 wins")

# Win condition for player 2
def playerTwoWin():
    pass

def main():
    gameSetup()
main()