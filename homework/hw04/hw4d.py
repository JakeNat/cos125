# File: hw4d.py
# Author: Jake Natalizia
# Date: October 23rd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Two nested while loops utilizing sentinel values.
# Collaboration: I did not collaborate with anyone.

def average(list):
    avg = sum(list) / len(list)
    return avg

def main():
    i = 0
    while i == 0:
        name = input("Hello, what is your name?")
        if name == "q":
            i = i + 1
            print("Goodbye")

        numList = []
        number = 0

        while number != -1 and name != "q":
            number = int(input("Hi " + name + ", enter a number:"))
            numList.append(number)
        if number == -1:
            roundedAvg = round(average(numList))
            print("The average for " + name + " is " + str(roundedAvg))
main()