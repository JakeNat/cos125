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
    a = 0

    # Checks for horizontal win
    for rows in board:
        for column in rows:
            b = a + 1
            c = b + 1
            d = c + 1

            # Prevents from checking past the board's index (horizontally)
            if d <= col:
                if rows[a] == P1_MARK and rows[b] == P1_MARK and rows[c] == P1_MARK and rows[d] == P1_MARK:
                    playerOneWin()                    
                elif rows[a] == P2_MARK and rows[b] == P2_MARK and rows[c] == P2_MARK and rows[d] == P2_MARK:
                    playerTwoWin()                    
                a += 1
            
            # Prevents from checking past the board's index (horizontally)
            elif d > col:
                a = 0
    
    # 'b' is set to the bottom row's index
    b = col - 1
    # Checks for vertical win
    for rows in board:
        a = 0
        for column in rows:
            c = b - 1
            d = c - 1
            e = d - 1
            
            # Prevents from checking past the board's index (vertically)
            if e >= 0:
                if board[b][a] == P1_MARK and board[c][a] == P1_MARK and board[d][a] == P1_MARK and board[e][a] == P1_MARK:
                    playerOneWin()
                elif board[b][a] == P2_MARK and board[c][a] == P2_MARK and board[d][a] == P2_MARK and board[e][a] == P2_MARK:
                    playerTwoWin()
                a += 1
            
            # Makes sure 'b' is reset before checking each row
            elif e < 0:
                b -= 1
            
            # Prevents from checking past the board's index (horizontally)
            elif a >= row:
                a = 0    
        
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