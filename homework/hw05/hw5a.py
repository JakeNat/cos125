# File: hw5a.py
# Author: Jake Natalizia
# Date: October 30th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Simulates up and down movement of a hailstone in a storm.
# Collaboration: I did not collaborate with anyone.

def oddHeight(height):
    # While height is odd
    while height % 2 != 0 and height != 1:
        # Multiply height by 3, add 1, print height
        height = (height * 3) + 1
        print("Hail is currently at height " + str(height))
        # If height is even
        if height % 2 == 0:
            evenHeight(height)

def evenHeight(height):
    # While height is even
    while height % 2 == 0:
        # Divide height by 2, print height
        height = height // 2
        print("Hail is currently at height " + str(height))
        # If height is odd, and isn't 1
        if height % 2 != 0 and height != 1:
            oddHeight(height)
        elif height == 1:
                print("The hailstone has stopped at height 1.")

def main():
    height = int(input("Enter the starting height of the hailstone:"))

    if height != 1:
        print("Hail is currently at height " + str(height))
        # If height is even
        if height % 2 == 0:
            evenHeight(height)
        # If height is odd
        elif height % 2 != 0 and height != 1:
            oddHeight(height)
    else:
        print("The hailstone has stopped at height 1.")
main()