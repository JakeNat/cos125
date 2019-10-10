# File: hw3a.py
# Author: Jake Natalizia
# Date: September 30th, 2019
# Section: B
# E-Mail: jacob.natalizia@umaine.edu
# Description: Reads a single float, prints the number and if it's positive/negative/equal to zero.
# Collaboration: I did not collaborate with anyone.

def main():
    float1 = float(input("Please enter a floating point number:"))
    if float1 == 0:
        print("The number " + str(float1) + " is equal to zero.")
    elif float1 > 0:
        print("The number " + str(float1) + " is positive.")
    elif float1 < 0:
        print("The number " + str(float1) + " is negative.")
main()