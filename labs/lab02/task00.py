# File: task00.py
# Author: Jake Natalizia
# Date: September 24th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Contains three different logic functions.
# Collaboration: I did not collaborate with anyone.

# Function 1
def GetUserName():
    name = input("What is your name?")
    return name

# Function 2
def HealCharacter(health, heal_amt):
    health = health + heal_amt
    if health >= 100:
        return 100
    else:
        return health

# Gravitational Constant
GRAV_CONST = G = (6.674 * 10**-11)

# Function 3
def GravForce(m1, m2, r):
    F = G * (m1 * m2) / r**2
    return F

# Calls each function and shows what each outputs.
def main():
    print(GetUserName())
    print(HealCharacter(60, 25))
    print(HealCharacter(90, 50))
    print(GravForce(200, 400, 70))
main()