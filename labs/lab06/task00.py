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

###############################################################################

formattedNames = []
listOfIDs = []
sortedNames = sorted(list_of_names)
sortedWages = sorted(list_of_wages, key=lambda x: x[1])
sortedHours = sorted(list_of_hours)

def formatNames():
    count = 0
    for names in sortedNames:
        while count < len(sortedNames):
            a = sortedNames[count]
            (id, name) = a
            formattedNames.append(name.lower().title())
            listOfIDs.append(id)
            count += 1

formattedWages = []

def formatWages():
    count = 0
    for wages in sortedWages:
        while count < len(sortedWages):
            a = sortedWages[count]
            (wage, id) = a
            formattedWages.append(wage)
            count += 1

formattedHours = []

def formatHours():
    count = 0
    for hours in sortedHours:
        while count < len(sortedHours):
            a = sortedHours[count]
            (id, hour) = a
            formattedHours.append(hour)
            count += 1

bonusList = []

def formatBonuses():
    count = 0
    for bonuses in BONUS_TABLE:
        while count < len(BONUS_TABLE):
            a = BONUS_TABLE[count]
            (hours, bonus) = a
            bonusList.append(bonus)
            count += 1

formattedBonuses = []

def getBonuses():
    for hours in formattedHours:
        if hours < 20:
            formattedBonuses.append(0.0)
        if hours >= 20 and hours < 30:
            formattedBonuses.append(15.0)
        if hours >= 30 and hours < 40:
            formattedBonuses.append(25.0)
        if hours >= 40 and hours < 50:
            formattedBonuses.append(35.0)
        if hours >= 50:
            formattedBonuses.append(50.0)

hourlyEarnings = []

def getHourlyEarnings():
    count = 0
    for wage in formattedWages:
        while count < len(formattedWages):
            earnings = (formattedWages[count] * formattedHours[count]) + formattedBonuses[count]
            hourlyEarnings.append(earnings)
            count += 1

def format_data():
    formatNames()
    formatWages()
    formatHours()
    formatBonuses()
    getBonuses()
    getHourlyEarnings()

    zipped = list(zip(listOfIDs, formattedNames, formattedWages, formattedHours, formattedBonuses, hourlyEarnings))
    for i in zipped:
        print(i)
format_data()