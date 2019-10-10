# File: task02.py
# Author: Jake Natalizia
# Date: October 1st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Three different blocks of code with an explanation of what's wrong with them (if there's anything).
# Collaboration: I did not collaborate with anyone.

# BLOCK 1
i = 1
while i != 100:
    i = i + 2
# Since 2 is always added to i, i will always be an odd number. Meaning it
# will never equal EXACTLY 100. This is an infinite loop.

# BLOCK 2
i = 0
while i < 10:
    astr = ""
    while i < 10:
        astr = astr + "," + str(i)
        i = i + 1
    print(astr)
# Nothing is inherently wrong with this code. My only concern with it is
# the extra comma that will come before the first actual value.

# BLOCK 3
def Sign(val):
    if val < 0:
        print "Negative"
    elif val > 0:
        print "Positive"
# Nothing prints because of the lack of parenthesis.