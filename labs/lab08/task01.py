# File: task00.py
# Author: Jake Natalizia
# Date: November 5th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Module with 5 lines of code
# Collaboration: I did not collaborate with anyone.

import random

print("Multiplies a specific number by a random integer between 1 and 50.")
randomInt = int(input("Please enter an integer."))
multiply = random.randrange(1,50)
print(str(randomInt) + " was multiplied by " + str(multiply) + ":")
print(randomInt * multiply)