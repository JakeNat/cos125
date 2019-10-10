# File: hw2a.py
# Author: Jake Natalizia
# Date: September 22nd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Calculates the average UMaine score for the first three football games.
# Collaboration: I did not collaborate with anyone.

def main():
    import math
    print("Hello, I will calculate the UMaine football average.")
    game_1 = int(input("What was the first score?"))
    game_2 = int(input("What was the second score?"))
    game_3 = int(input("What was the third score?"))
    averageScore = math.floor((game_1 + game_2 + game_3) / 3)
    print("The average UMaine score in the first three games was " + str(averageScore) + ".")
main()