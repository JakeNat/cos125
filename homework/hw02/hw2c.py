# File: hw2c.py
# Author: Jake Natalizia
# Date: September 22nd, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Converts number grades to letter grades.
# Collaboration: I did not collaborate with anyone.

def printLetterGradeFromNumber(grade):
        if grade >= 90:
            return "A"
        if grade >= 80 and grade < 90:
            return "B"
        if grade >= 70 and grade < 80:
            return "C"
        if grade >= 60 and grade < 70:
            return "D"

def main():
    print("Hello, I will convert numbers into letter grades.")
    grade = int(input("What was the first number grade?"))
    letterGrade = printLetterGradeFromNumber(grade)
    print("The student gets a " + str(letterGrade) + ".")

    grade = int(input("What was the second number grade?"))
    letterGrade = printLetterGradeFromNumber(grade)
    print("The student gets a " + str(letterGrade) + ".")

    grade = int(input("What was the third number grade?"))
    letterGrade = printLetterGradeFromNumber(grade)
    print("The student gets a " + str(letterGrade) + ".")

    grade = int(input("What was the fourth number grade?"))
    letterGrade = printLetterGradeFromNumber(grade)
    print("The student gets a " + str(letterGrade) + ".")

    grade = int(input("What was the fifth number grade?"))
    letterGrade = printLetterGradeFromNumber(grade)
    print("The student gets a " + str(letterGrade) + ".")
main()