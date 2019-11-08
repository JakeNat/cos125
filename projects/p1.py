# File: p1.py
# Author: Jake Natalizia
# Date: November 4th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Connect Four
# Collaboration: I did not collaborate with anyone.

# CONSTANTS
P1_MARK = "x"
P2_MARK = "o"

# Gets board/game parameters
def gameSetup():
    # Gets row size
    rowSize = ""
    while rowSize == "":
        rowSize = int(input("Please enter your desired row size: "))
        if rowSize < 5:
            print("Row size must be at least 5.")
            rowSize = ""

    # Get column size
    columnSize = ""
    while columnSize == "":
        columnSize = int(input("Please enter your desired column size: "))
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
def onePlayer(row, col):
    # Prints out board
    board = [["_"] * row for i in range(col)]

    # 1 for Player 1, 2 for Player 2
    turnCounter = 0
    while turnCounter == 1:
        columnChoice = int(input("PLAYER 1\n\tChoose a column: "))
        board[col-1][columnChoice-1] = P1_MARK
        turnCounter += 2
    while turnCounter == 2:
        # !!!! Call computer function !!!!
        print("Computer's turn")
    for element in board:
        for i in element:
            print(i, end=' ')
        print("")

# For two players playing each other
def twoPlayers(row, col):
    # Prints out board
    board = [["_"] * row for i in range(col)]

    totalMoves = row * col

    # Limits amount of turns to totalMoves
    for i in range(0, totalMoves - 1):
        # 1 for Player 1, 2 for Player 2
        turnCounter = 1
        while turnCounter == 1:
            columnChoice = int(input("PLAYER 1\n\tChoose a column: ")) - 1

            # To keep track of whats in each column
            columnCount = [0 * 1 for i in range(row)]
            print(columnCount)

            # To check if an index is assigned an 'x' or 'o' !!! FIX !!!
            for row in board:
                for index in row:
                        if index == P1_MARK or index == P2_MARK:
                            columnCount[columnChoice] += 1
                            board[col-(columnCount[columnChoice])] = P1_MARK
            
            updateBoard(board)
            turnCounter += 1
        
        while turnCounter == 2:
            columnChoice = int(input("PLAYER 2\n\tChoose a column: ")) - 1
            board[col-1][columnChoice] = P2_MARK
            updateBoard(board)
            turnCounter -= 1

# Prints the board in its current state
def updateBoard(board):
    for element in board:
        for i in element:
            print(i, end=' ')
        print("")


def main():
    gameSetup()
main()