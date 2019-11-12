# File: task00.py
# Author: Jake Natalizia
# Date: November 5th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Review
# Collaboration: I did not collaborate with anyone.

def functionA(a,b):
    if a == 0 and b == 0:
        print("ERROR")
    elif a < 0 or b < 0:
        print("ERROR")

def functionB(books,title):
    if title in books:
        return True
    else:
        return False

def functionC(a):
    charCount = range(1,20)
    if len(a) < len(charCount):
        a = a + "." * (20 - len(a))
    print(a)

def main():
    a = "123456789"
    functionC(a)
main()