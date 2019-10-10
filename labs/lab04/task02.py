# File: task02.py
# Author: Jake Natalizia
# Date: October 10th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: First function swaps the first and last elements in a list. Second function finds and returns the minimum value in a list.
# Collaboration: I did not collaborate with anyone.

def swap(list):
    a = list.pop(0)
    b = list.pop(len(list) - 1)
    list.append(a)
    list.insert(0, b)

def listMin(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    print(min)