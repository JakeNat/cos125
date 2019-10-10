# File: task02.py
# Author: Jake Natalizia
# Date: September 17th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Determines your post office box number based on last name, street number, and zip code.
# Collaboration: I did not collaborate with anyone.

lastName = input('What is your name?')
streetNumber = input('What is your street number?')
zipCode = input('What is your zip code?')
postBoxNumber = (len(lastName) * 3) + (pow(int(streetNumber), 3)) + (int(zipCode) / 10)
postBoxNumber = int((postBoxNumber % 211))
print("Natalizia " + str(postBoxNumber))