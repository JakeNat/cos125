# File: hw5b.py
# Author: Jake Natalizia
# Date: October 30th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Counts down from 101 to 1. Prints specific messages for certain conditions.
# Collaboration: I did not collaborate with anyone.

def main():
    for i in range(101, 0, -1):
        if i % 5 == 0 and i % 6 != 0:
            print("Where do you see yourself in five years?")
        elif i % 6 == 0 and i % 5 != 0:
            print("I'll do six impossible things before breakfast.")
        elif i % 5 == 0 and i % 6 == 0:
            print("Thirty days hath September.")
        else:
            print(i)
main()