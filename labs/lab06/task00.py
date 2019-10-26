# File: task00.py
# Author: Jake Natalizia
# Date: October 22nd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: 
# Collaboration: I did not collaborate with anyone.

# LAB 6

# Example output for Mary Beth Smith
# 0,Mary_Beth_Smith,$10.5,40,$35,$455,

###############################################################################

# CONST BONUS TABLES
# (Hours, Bonus amt)
# An employee receives a bonus based on the number of hours worked.
# Find the tuple in the table with highest hours that is less than
# or equal to the employees hours worked.
# Example: James worked 33.5 hours. His bonus is 25
BONUS_TABLE = [
    (20,15.0),
    (30,25.0),
    (40,35.0),
    (50,50.0)
]

# names: list of tuples (ID,NAME)
# wages: list of tuples (WAGE,ID)
# hours: list of tuples (ID,HOURS)
def format_data(names, wages, hours):
    # Use this function as the string point of your program
    # You may add other helper functions as you see fit, but
    # it is not required.

    # REMINDER: This function must return a single string
    #   of CSV data for the test code below to work.
    #   Format:
    #   "ID,NAME,WAGE,HOURS,BONUS,EARNINGS\n"
    pass

###############################################################################
# TEST CODE - DO NOT CHANGE

# (ID,NAMES)
list_of_names = [
    (0,"Mary beth SmitH"),
    (2,"paTricia t jOHNSON"),
    (45,"LiNda Williams"),
    (178,"baRbarA beth browN"),
    (3,"elizABeth MiLLer"),
    (9,"JenNifer DaviS"),
    (83,"Maria rodrigueZ"),
    (22,"sUsaN MartiNEZ"),
    (38,"margAret q AndERSon")
]

# (WAGES,ID)
list_of_wages = [
    (14.0,3),
    (13.5,2),
    (18.0,38),
    (12.0,45),
    (10.5,0),
    (20.0,178),
    (17.25,83),
    (13.5,22),
    (9.75,9)
]

# (ID,HOURS)
list_of_hours = [
    (2,39),
    (0,40),
    (22,24.25),
    (9,41.25),
    (83,37.0),
    (3,43.5),
    (38,45),
    (178,51),
    (45,12.5)
]

# csv_data = format_data(list_of_names, list_of_wages, list_of_hours)
# print(csv_data)

formattedNames = []
listOfIDs = []

def formatNames():
    count = 0
    for i in list_of_names:
        while count < len(list_of_names):
            a = list_of_names[count]
            (id, name) = a
            formattedNames.append(name.lower().title())
            listOfIDs.append(id)
            count += 1
formatNames()
print(formattedNames)
print(listOfIDs)