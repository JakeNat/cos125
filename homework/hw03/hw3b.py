# File: hw3b.py
# Author: Jake Natalizia
# Date: September 30th, 2019
# Section: B
# E-Mail: jacob.natalizia@umaine.edu
# Description: Gives recycling advice based on how many bottles and cans were recycled/used.
# Collaboration: I did not collaborate with anyone.

def respondToBottles(cansUsed, cansRecycled):
    if cansRecycled < cansUsed:
        print("Please try to recycle all of the bottles you use.")
    elif cansRecycled == cansUsed and cansRecycled > 0 and cansUsed < 6:
        print("Good job recycling all your cans and bottles!")
    elif cansRecycled > cansUsed:
        print("How did you do that? Impressive!")
    elif cansRecycled == 0:
        print("Try to recycle some bottles and cans.")
    elif cansUsed > 5:
        print("You should probably get a reusable bottle.")

def main():
    print("Hello, I will give recycling advice.")
    cansUsed     = int(input("How many bottles/cans did you use today?"))
    cansRecycled = int(input("How many did you recycle?"))
    respondToBottles(cansUsed, cansRecycled)
main()