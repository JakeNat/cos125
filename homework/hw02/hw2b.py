# File: hw2b.py
# Author: Jake Natalizia
# Date: September 22nd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Calculates your final grade based on weights for different assignments.
# Collaboration: I did not collaborate with anyone.

def main():
    print("Hello, I will calculate your grade.")
    homeworkWeight = float(input("What is the homework weight?"))
    homeworkGrade  = int(input("What is your homework grade?"))
    homeworkCalc   = (homeworkWeight * homeworkGrade)
    projectWeight  = float(input("What is the project weight?"))
    projectGrade   = int(input("What is your project grade?"))
    projectCalc    = (projectWeight * projectGrade)
    quizWeight     = float(input("What is the surveys/quizzes/in-class weight?"))
    quizGrade      = int(input("What is your surveys/quizzes/in-class grade?"))
    quizCalc       = (quizWeight * quizGrade)
    labWeight      = float(input("What is the lab weight?"))
    labGrade       = int(input("What is your lab grade?"))
    labCalc        = (labWeight * labGrade)
    hourlyWeight   = float(input("What is the hourly exam weight?"))
    hourlyGrade    = int(input("What is your hourly exam grade?"))
    hourlyCalc     = (hourlyWeight * hourlyGrade)
    examWeight     = float(input("What is the final exam weight?"))
    examGrade      = int(input("What is your final exam grade?"))
    examCalc       = (examWeight * examGrade)
    finalGrade     = homeworkCalc + projectCalc + quizCalc + labCalc + hourlyCalc + examCalc
    print("Your grade is " + str(int(finalGrade)) + ".")
main()