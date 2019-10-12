# File: hw4a.py
# Author: Jake Natalizia
# Date: October 12th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Asks for a number. Continues to ask until an odd number is inputted.
# Collaboration: I did not collaborate with anyone.

def main():
    i = 0
    while i == 0:
        prompt = int(input("Please enter a number."))
        if (prompt % 2 == 0):
            print("That number is not odd.")
            i = 0
        elif (prompt % 2 != 0):
            print("That number is odd.")
            i = 1
main()