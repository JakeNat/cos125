# File: task01.py
# Author: Jake Natalizia
# Date: September 17th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Runs each block of code from Task 01.
# Collaboration: I did not collaborate with anyone.

# Code Block 1

a = 100
x = 10
z = 2.0
x = int(x/z) + x
x = x - (z - 1)
a = a - x
print(a)

# Code Block 2

a = '100'
b = '20'
c = '3'
a = a + b + c
b = int(c) + 0.1
a = int(float(a) + b)
print(a)

# For code block 2, the first time I ignored the fact that a, b and c were strings. 
# I did actual addition rather than concatenation.
# I corrected myself the second time through.

# Code Block 3

a = len('five') * 2
b = 1.5
c = (a // b)
a = ( c % 2 + 1 ) * (1 + b)
print(a)

# I misinterpreted what len() did and what % did
# After going through a second and third time, I understand everything now.