# File: task00.py
# Author: Jake Natalizia
# Date: November 12th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Analyze Data
# Collaboration: I did not collaborate with anyone.

def main():
    samples = open('labs/lab09/samples.txt','r')
    samplesList = samples.readlines()

    for line in range(0,len(samplesList)):
        samplesList[line] = int(samplesList[line])

    length = str(len(samplesList))
    minimum = str(min(samplesList))
    maximum = str(max(samplesList))
    sums = str(sum(samplesList))

    samples.close()

    samples = open('labs/lab09/samples.txt','a')

    samples.write(length + '\n')
    samples.write(minimum + '\n')
    samples.write(maximum + '\n')
    samples.write(sums + '\n')

    samples.close()
main()