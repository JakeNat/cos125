# File: task01.py
# Author: Jake Natalizia
# Date: October 1st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Three different loops. Each is in their own function to easily see how each runs.
# Collaboration: I did not collaborate with anyone.

def task1_1():
    loopCounter = int(input("Press 0 to start the first loop."))
    if loopCounter != 0:
        print("Please enter a 0.")
        loopCounter = 10
    while loopCounter != 10:
        print(loopCounter/1)
        loopCounter = loopCounter + 1

def task1_2():
    i = 10 + int(input("Press 0 to start the next loop."))
    if i != 10:
        print("Please enter a 0.")
        i = 0
    while i != 0:
        print(i)
        i = i - 1

def task1_3():
    n = 171 + int(input("Press 0 to start the last loop."))
    if n != 171:
        print("Please enter a 0.")
        n = 0
    v = 233
    count = 0
    while n != 0:
        n = n - 1
        while v != 0:
            v = v - 1
            count = count + 1
    print(count)

def main():
    task1_1()
    task1_2()
    task1_3()
main()