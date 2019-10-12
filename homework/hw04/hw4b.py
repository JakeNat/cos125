# File: hw4b.py
# Author: Jake Natalizia
# Date: October 12th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Triples all values in a list. Prints the odd triples, says if a tripled value is even. Sums all odd values.
# Collaboration: I did not collaborate with anyone.

def triple(list):
    sumOfOdds = 0
    for i in list:
        index = list.index(i)
        print("Value #" + str(index+1) + " is: " + str(i))
        triple_i = i * 3
        if ((triple_i) % 2) != 0:
            print("Value #" + str(index+1) + " tripled is: " + str(i * 3))
            sumOfOdds = sumOfOdds + triple_i
        elif ((i * 3) % 2) == 0:
            print("Value #" + str(index+1) + " tripled is even!")
    print("The sum of the odd numbers is " + str(sumOfOdds))
    

def main():
    myList = [5, 8, 11, 14, 17]
    triple(myList)
main()