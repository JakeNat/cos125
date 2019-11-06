# File: p1.py
# Author: Jake Natalizia
# Date: November 4th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Connect Four
# Collaboration: I did not collaborate with anyone.

# Gets board parameters from user
def getBoard():
    # Get row size
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
    return rowSize, columnSize

def gameType():
    print("-"*35)
    print("Do you want to play against the computer? Y/N")
    gameChoice = ""
    while gameChoice == "":
        gameChoice = input("Y for YES, N for NO: ")
        if gameChoice == "y":
            print("SELECTED: Player vs. Player")
            onePlayer()
        elif gameChoice == "n":
            print("SELECTED: Player vs. Computer")
            twoPlayers()
        else:
            print("Please enter a \"y\" or a \"n\".")
            gameChoice = ""

# Draws board
def drawBoard(row, col):
    board = [["_"] * row] * col
    for element in board:
        for i in element:
            print(i, end=' ')
        print()

# For playing against the computer
def onePlayer():
    pass

# For two players playing each other
def twoPlayers():
    pass

def main():
    # Stores row/col sizes from getBoard()
    rowSize, columnSize = getBoard()
    drawBoard(rowSize, columnSize)
main()