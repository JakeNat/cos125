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
    print("Welcome to Connect Four")
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

    numOfTurns = 0

    # Limits amount of turns to totalMoves
    for i in range(0, totalMoves - 1):
        # Player 1 goes when 1, Player 2 goes when 2
        turnCounter = 1

        # PLAYER ONE'S TURN
        while turnCounter == 1:
            updateBoard(board)
            checkEndGame(board,row,col)

            # Checks for tie condition
            if numOfTurns == totalMoves:
                drawCondition()

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
                numOfTurns += 1
                turnCounter += 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                numOfTurns += 1
                turnCounter += 1
        
        # COMPUTER'S TURN
        while turnCounter == 2:
            updateBoard(board)
            checkEndGame(board,row,col)

            # Checks for tie condition
            if numOfTurns == totalMoves:
                drawCondition()

            # Input validation for column choice
            columnChoice = 0
            while columnChoice == 0 or columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                columnChoice = random.randrange(1,col+1)
                if columnChoice > row or columnCount[columnChoice-1] >= col or columnChoice == 0:
                    columnChoice == 0
            print("COMPUTER CHOOSES COLUMN " + str(columnChoice))

            # Decremented to easily reference list indexes
            columnChoice -= 1

            # If the player's selection is already marked, mark the row above it
            if board[col-(columnCount[columnChoice])][columnChoice] == P1_MARK or board[col-(columnCount[columnChoice])][columnChoice] == P2_MARK:
                columnCount[columnChoice] += 1
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                numOfTurns += 1
                turnCounter -= 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                numOfTurns += 1
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

    numOfTurns = 0

    # Limits amount of turns to totalMoves
    for i in range(0, totalMoves - 1):
        # Player 1 goes when turnCounter is 1, Player 2 goes when turnCounter is 2
        turnCounter = 1

        # PLAYER ONE'S TURN
        while turnCounter == 1:
            updateBoard(board)
            checkEndGame(board,row,col)

            # Checks for tie condition
            if numOfTurns == totalMoves:
                drawCondition()

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
                numOfTurns += 1
                turnCounter += 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P1_MARK
                numOfTurns += 1
                turnCounter += 1
        
        # PLAYER TWO'S TURN
        while turnCounter == 2:
            updateBoard(board)
            checkEndGame(board,row,col)

            # Checks for tie condition
            if numOfTurns == totalMoves:
                drawCondition()

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
                numOfTurns += 1
                turnCounter -= 1

            # If the player's selection is empty, mark it
            elif board[col-(columnCount[columnChoice])][columnChoice] != P1_MARK and board[col-(columnCount[columnChoice])][columnChoice] != P2_MARK:
                board[col-(columnCount[columnChoice])][columnChoice] = P2_MARK
                numOfTurns += 1
                turnCounter -= 1    

# Prints the board in its current state
def updateBoard(board):
    for element in board:
        for i in element:
            print(i, end=' ')
        print("")

def checkEndGame(board,row,col):
    # Checks for vertical win
    for a in range(col):
        for b in range(row):
            # Keeps iteration within the board's range
            if (a - 3) >= 0 and b < row:
                if board[a][b] == P1_MARK and board[a-1][b] == P1_MARK and board[a-2][b] == P1_MARK and board[a-3][b] == P1_MARK:
                    playerOneWin()
                elif board[a][b] == P2_MARK and board[a-1][b] == P2_MARK and board[a-2][b] == P2_MARK and board[a-3][b] == P2_MARK:
                    playerTwoWin()
    
    # Checks for horizontal win
    for a in range(col):
        for b in range(row):
            # Keeps iteration within the board's range
            if a < col and (b + 3) < row:
                if board[a][b] == P1_MARK and board[a][b+1] == P1_MARK and board[a][b+2] == P1_MARK and board[a][b+3] == P1_MARK:
                    playerOneWin()
                elif board[a][b] == P2_MARK and board[a][b+1] == P2_MARK and board[a][b+2] == P2_MARK and board[a][b+3] == P2_MARK:
                    playerTwoWin()

    # Checks for diagonal win (up and right)
    for a in range(col):
        for b in range(row):
            # Keeps iteration within the board's range
            if (a - 3) >= 0 and (b + 3) < row:
                if board[a][b] == P1_MARK and board[a-1][b+1] == P1_MARK and board[a-2][b+2] == P1_MARK and board[a-3][b+3] == P1_MARK:
                    playerOneWin()
                elif board[a][b] == P2_MARK and board[a-1][b+1] == P2_MARK and board[a-2][b+2] == P2_MARK and board[a-3][b+3] == P2_MARK:
                    playerTwoWin()
    
    # Checks for diagonal win (up and left)
    for a in range(col):
        for b in range(row):
            # Keeps iteration within the board's range
            if (a - 3) >= 0 and (b - 3) >= 0:
                if board[a][b] == P1_MARK and board[a-1][b-1] == P1_MARK and board[a-2][b-2] == P1_MARK and board[a-3][b-3] == P1_MARK:
                    playerOneWin()
                elif board[a][b] == P2_MARK and board[a-1][b-1] == P2_MARK and board[a-2][b-2] == P2_MARK and board[a-3][b-3] == P2_MARK:
                    playerTwoWin()  
        
# Win condition for player 1
def playerOneWin():
    print("Player 1 wins")
    playAgain()

# Win condition for player 2
def playerTwoWin():
    print("Player 2 wins")
    playAgain()

# Draw condition
def drawCondition():
    print("The game has ended in a tie.")
    playAgain()

# Prompts for new game
def playAgain():
    print("Do you want to play again? Y/N")
    startNewGame = ""
    while startNewGame == "":
        # Start a new game
        startNewGame = input("\tY for YES, N for NO: ")
        if startNewGame == "y":
            print("STARTING NEW GAME...")
            gameSetup()
        # Exit game
        elif startNewGame == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter a \"y\" or a \"n\".")
            startNewGame = ""

def main():
    gameSetup()
main()