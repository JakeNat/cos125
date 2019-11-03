# File: task00.py
# Author: Jake Natalizia
# Date: October 29th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: The Interactive CPU
# Collaboration: I did not collaborate with anyone.

def main():
    registerList = [None]*10
    
    count = 0
    while count == 0:
        userInput = input(">>>")
        command = userInput[0]
        
        if command == "s":
            registerNum = int(userInput[2])
            data = userInput[4:]
            del registerList[registerNum]
            registerList.insert(registerNum, data)
        elif command == "d":
            registerNum = int(userInput[2])
            data = userInput[4:]
            registerList.insert(registerNum, None)
            del registerList[registerNum + 1]
        elif command == "p":
            print(registerList)
        elif command == "q":
            count += 1
    else:
        print("Goodbye.")
main()