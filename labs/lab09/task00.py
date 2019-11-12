# File: task00.py
# Author: Jake Natalizia
# Date: November 12th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Find Data
# Collaboration: I did not collaborate with anyone.

def main():
    data = open('labs/lab09/lab9_data.txt','r')
    samples = open('labs/lab09/samples.txt','w')

    for line in data:
        if int(line) > 1000000:
            samples.writelines(line)

    data.close()
    samples.close()
main()