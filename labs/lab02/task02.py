# File: task02.py
# Author: Jake Natalizia
# Date: September 24th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Simple text game that has 3 different outcomes.
# Collaboration: I did not collaborate with anyone.

leftDoor  = "L"
rightDoor = "R"
frontDoor = "F"

def RightDoor():
        print("You open the right door.")
        print("You step through the door and fall 60 meters. Splat.")
        print("You lose.")

def LeftDoor():
    print("You open the left door.")
    print("Your eyes meet a chest in the center of the room.")
    print("Inside the chest is a map of the building, accompanied by hundreds of thousands of dollars.")
    print("Congratulations. You win!")

def FrontDoor():
    print("You open the door in front of you.")
    print("A dragon awaits your arrival. You are reduced to a pile of ash.")
    print("You lose.")

def main():
    print("You wake up in a room.")
    print("There are doors to your left, to your right, and in front of you.")
    chooseDoor = input("Press [L] to go left. Press [R] to go right. Press [F] to go forward.")
    if chooseDoor.upper() == leftDoor:
        LeftDoor()
    if chooseDoor.upper() == rightDoor:
        RightDoor()
    if chooseDoor.upper() == frontDoor:
        FrontDoor()
    print("Thanks for playing!")
main()