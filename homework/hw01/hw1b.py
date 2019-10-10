# File: hw1b.py
# Author: Jake Natalizia
# Date: September 17th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Determines the total cost, with tax, of a given amount of ice cream bars.
# Collaboration: I did not collaborate with anyone.

price = int(input("How much is this ice cream bar?"))
totalCost = (price * 3)
totalCost = round(totalCost + (totalCost * 0.055), 2)
print("I would like three bars. Here is $" + str(totalCost) + ".")
print("Thank you.")