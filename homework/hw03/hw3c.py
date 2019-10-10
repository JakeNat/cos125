# File: hw3c.py
# Author: Jake Natalizia
# Date: October 1st, 2019
# Section: B
# E-Mail: jacob.natalizia@umaine.edu
# Description: Tells if UMaine's women's soccer team won their game based on how many goals both teams scored.
# Collaboration: I did not collaborate with anyone.

def printGameResult(homeScore, awayScore):
    if homeScore > awayScore:
        print("UMaine won this game!")
        return True
    elif homeScore < awayScore:
        print("UMaine lost this game.")
        return False
    elif homeScore == awayScore:
        print("UMaine tied this game.")
        return False

def main():
    counter = 0
    print("Hello, I will calculate the UMaine women's soccer summary for the first seven games.")
    # Game 1
    homeScore = input("What did UMaine score in the first game?")
    awayScore = input("What did the opponent score in the first game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 2
    homeScore = input("What did UMaine score in the second game?")
    awayScore = input("What did the opponent score in the second game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 3
    homeScore = input("What did UMaine score in the third game?")
    awayScore = input("What did the opponent score in the third game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 4
    homeScore = input("What did UMaine score in the fourth game?")
    awayScore = input("What did the opponent score in the fourth game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 5
    homeScore = input("What did UMaine score in the fifth game?")
    awayScore = input("What did the opponent score in the fifth game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 6
    homeScore = input("What did UMaine score in the sixth game?")
    awayScore = input("What did the opponent score in the sixth game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    # Game 7
    homeScore = input("What did UMaine score in the seventh game?")
    awayScore = input("What did the opponent score in the seventh game?")
    printGameResult(homeScore, awayScore)
    if printGameResult(homeScore, awayScore) == True:
        counter = counter + 1
    print("UMaine has won " + str(counter) + " games so far.")
main()