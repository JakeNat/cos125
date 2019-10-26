# File: hw4c.py
# Author: Jake Natalizia
# Date: October 22nd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Analyzes scores of UMaine's soccer team. Determines the winner of each game and prints how many UMaine won.
# Collaboration: I did not collaborate with anyone.

# Gets result of game based on score
def printGameResults(home, away):
    if home > away:
        print("UMaine won this game!")
        return True
    if home < away:
        print("UMaine lost this game.")
        return False
    if home == away:
        print("This game ended in a tie.")
        return False

def main():
    # Asks user how many games were played
    numOfGames = int(input("Enter the number of games:"))
    if numOfGames == 0:
        print("UMaine has not played any games yet.")
    
    # Keeps track of UMaine wins and for each game played, asks for the score
    maineWins = 0
    for i in range(numOfGames):
        homeScore = int(input("What did UMaine score in the game?"))
        awayScore = int(input("What did the opponent score in the game?"))
        printGameResults(homeScore, awayScore)
        if homeScore > awayScore:
            maineWins += 1

    print("UMaine won " + str(maineWins) + " games.")
main()