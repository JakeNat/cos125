# File: task04.py
# Author: Jake Natalizia
# Date: September 17th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Calculates your distance from home and your average walking speed, based on the distance of your two paths.
# Collaboration: I did not collaborate with anyone.

pathOne = input("How far is your first path, in meters?")
pathTwo = input("How far is your second path, in meters?")
totalPath = pow((pow(float(pathOne), 2) + pow(float(pathTwo), 2)), 0.5)
totalPath = round(totalPath, 2)
print("You are currently " + str(totalPath) + " meters from home.")

# For step 3, rather than adding an additional calculation, you can
# just add 2.7 km to your original 3.6 km distance, since they're both westward.
# Now you get a total of 6.3 kilometers (6300 meters) west, which can be pathOne.
# Same concept for the time taken. Direction is superfluous. You only need the total time.

timeTaken = input("How long did it take to complete your journey, in hours?")
averageWalkingSpeed = (float(totalPath) / float(timeTaken)) / 1000
averageWalkingSpeed = round(averageWalkingSpeed, 2)
print("Your average walking speed was " + str(averageWalkingSpeed) + " kilometers per hour.")