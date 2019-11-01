# File: hw5d.py
# Author: Jake Natalizia
# Date: October 31st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description:
# Collaboration: I did not collaborate with anyone.

def drawBox(width, height, outline, fill):
    # Top of box
    print(outline*width)

    # "Body" of box, deals with height
    getHeight = range(height-2)
    for i in getHeight:
        print(outline + (fill * (width - 2)) + outline)

    # Bottom of box
    print(outline*width)

def drawTriangle(width, height, fill):
    getHeight = range(height)
    for i in getHeight:
        meanList = list(range(height))
        print(meanList[height])

def middleNumber(num):
    mean = ((num - 1) / 2) + 1
    return mean

def getPositiveNumber():
    # Ask for triangle/box height
    posNum = 0
    while posNum <= 0:
        print("-"*35)
        print("Positive integers only, please.")
        posNum = int(input("Please enter the triangle/box height:"))
    return posNum

def getOddPositiveNumber():
    # Ask for triangle base width
    posOddNum = 0
    while posOddNum <= 0 or posOddNum % 2 == 0:
        print("-"*35)
        print("Positive, odd integers only.")
        posOddNum = int(input("Please enter the triangle's base width:"))
    return posOddNum

def main():
    shapePrompt = ""
    while shapePrompt != "quit":
        print("-"*35)
        # Ask what shape to draw
        print("Press 1 for 'square'")
        print("Press 2 for 'triangle'")
        print("Type 'quit' to quit")
        shapePrompt = input("Choose a shape:")
        if shapePrompt == "1":
            print("-"*35)
            print("You have selected 'square'.")
            # Gets width of box
            width = int(input("Please enter the width of the box:"))
            print("-"*35)
            # Gets symbol for box outline
            outline = input("Please enter a symbol for the box outline:")
            print("-"*35)
            # Gets symbol for box fill
            fill = input("Please enter a symbol for the box fill:")
            print("-"*35)
            # Draw the box, also asks for height input
            drawBox(width, getPositiveNumber(), outline, fill)

        elif shapePrompt == "2":
            print("-"*35)
            print("You have selected 'triangle'.")
            # Get height
            getPositiveNumber()
            # Get base width
            print(getOddPositiveNumber())
            # Gets symbol for triangle fill
            fill = input("Please enter a symbol for the triangle fill:")

            drawTriangle(getOddPositiveNumber(), getPositiveNumber, fill)
        else:
            print("Please make a valid choice.")
main()