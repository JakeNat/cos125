# File: task00.py
# Author: Jake Natalizia
# Date: October 1st, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Finds the maximum value of three given numbers, evaluates if a password is valid (has more than 8 characters).
# Collaboration: I did not collaborate with anyone.

def MaxOfThree(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        return val1
    elif val2 > val1 and val2 > val3:
        return val2
    elif val3 > val1 and val3 > val2:
        return val3

def NewPassword(old_password):
    newPassword = input("Enter a new password.")
    if len(newPassword) < 8:
        return old_password
    elif len(newPassword) >= 8:
        return newPassword

def main():
    print("I will find the maximum value of three numbers.")
    input_1 = input("What is the first number?")
    input_2 = input("What is the second number?")
    input_3 = input("What is the third number?")
    print(MaxOfThree(input_1, input_2, input_3))

    old_password = input("Enter your current password.")
    print(NewPassword(old_password))
main()