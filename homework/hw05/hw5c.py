# File: hw5c.py
# Author: Jake Natalizia
# Date: October 31st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Draws a box with a given height and width.
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

def main():
    # Width of box
    width = int(input("Please enter the width of the box:"))

    # Height of box
    height = int(input("Please enter the height of the box:"))

    # Symbol for box outline
    outline = input("Please enter a symbol for the box outline:")

    # Symbol for box fill
    fill = input("Please enter a symbol for the box fill:")

    drawBox(width, height, outline, fill)
main()