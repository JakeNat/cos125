# File: hw3d.py
# Author: Jake Natalizia
# Date: October 1st, 2019
# Section: B
# E-Mail: jacob.natalizia@umaine.edu
# Description: Helps decide your major based on preferences.
# Collaboration: I collaborated with/helped Jamen Neptune.

def csMajor(problem, helping, create, money):
    if problem == True or helping == True or create == True or money == True:
        print("You should consider computer science.")

def socialWork(problem, helping, create, money):
    if problem == True and money == False:
        print("You should consider social work.")

def teachMajor(problem, helping, create, money):
    if helping == True and money == False:
        print("You should consider teaching.")

def artMajor(problem, helping, create, money):
    if create == True and money == False:
        print("You should consider art.")

def businessMajor(problem, helping, create, money):
    if money == True:
        print("You should consider business.")

def main():
    print("Hello, I will help you pick a major.")
    # Problem Solving
    probSolve = input("Do you like problem solving?").lower()
    if "yes" in probSolve:
        probSolve = True
    elif "no" in probSolve:
        probSolve = False
    # Helping Others
    helpOthers = input("Do you like to help others?").lower()
    if "yes" in helpOthers:
        helpOthers = True
    elif "no" in helpOthers:
        helpOthers = False
    # Creating Things
    createThings = input("Do you like to create?").lower()
    if "yes" in createThings:
        createThings = True
    elif "no" in createThings:
        createThings = False
    # Making Money
    makeMoney = input("Do you like to make money?").lower()
    if "yes" in makeMoney:
        makeMoney = True
    elif "no" in makeMoney:
        makeMoney = False
    csMajor(probSolve, helpOthers, createThings, makeMoney)
    socialWork(probSolve, helpOthers, createThings, makeMoney)
    teachMajor(probSolve, helpOthers, createThings, makeMoney)
    artMajor(probSolve, helpOthers, createThings, makeMoney)
    businessMajor(probSolve, helpOthers, createThings, makeMoney)
main()