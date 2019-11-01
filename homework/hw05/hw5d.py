# File: hw5d.py
# Author: Jake Natalizia
# Date: November 1st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Draws triangles and boxes based on user's specifications.
# Collaboration: I did not collaborate with anyone.

def mean(num):
    mean = ((num - 1) // 2)
    return mean

def drawBox(width, height, outline, fill):
    # Top of box
    print(outline*width)

    # "Body" of box, deals with height
    getHeight = range(height-2)
    for i in getHeight:
        print(outline + (fill * (width - 2)) + outline)

    # Bottom of box
    print(outline*width)

def drawTriangle(base, height, fill, outline):
    getHeight = range(height-2)
    space = ' '
    midNum = mean(base) - 1
    fillSpace = 1
    # Top of triangle
    print((space * (midNum + 1) + outline + (space * midNum)))

    # 'Body' of triangle
    for i in getHeight:
        print((space * midNum) + outline + (fill * (fillSpace)) + outline + (space * midNum))
        midNum -= 1
        fillSpace += 2
    
    # Base of triangle
    print(outline * base)

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
    count = 0
    while count == 0:
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
            # Gets symbol for box outline
            print("-"*35)
            outline = input("Please enter a symbol for the box outline:")
            # Gets symbol for box fill
            print("-"*35)
            fill = input("Please enter a symbol for the box fill:")
            # Draw the box, also asks for height input
            print("-"*35)
            drawBox(width, getPositiveNumber(), outline, fill)

        elif shapePrompt == "2":
            print("-"*35)
            print("You have selected 'triangle'.")
            # Gets symbol for triangle outline
            print("-"*35)
            outline = input("Please enter a symbol for the triangle outline:")
            # Gets symbol for triangle fill
            print("-"*35)
            fill = input("Please enter a symbol for the triangle fill:")

            drawTriangle(getOddPositiveNumber(), getPositiveNumber(), fill, outline)
        elif shapePrompt == "quit":
            print("-"*35)
            print("Goodbye.")
            print("-"*35)
            count += 1
        else:
            print("-"*35)
            print("Please make a valid choice.")
main()