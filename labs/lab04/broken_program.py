# LAB 4 - Broken Program
# by ZSH v0.1

# This program does not work. It it supposed to be a simple
# program that asks the user to enter the hours worked for
# a hard-coded list of employees.

# Fix it, add your name to the list of employees, 
# and submit a screenshot of the output.

#######################################################################
# FUNCTION DEFS

# Prints a list of names in a nice way
def PrettyPrintNames(names):
    astr = ""
    i = 0
    while i <= len(names):
        # Just add the first thing
        if i == 0:
            astr = names[i]
        # If it's the last, give an 'and'
        elif i == len(names)-1 and len(names) > 1:
            astr = astr + " and " + names[i]
        elif i < len(names)-1:
        # Somewhere in the middle
            astr = astr + ", " + names[i]


        i = i + 1

    if len(astr) > 0:
        print(astr)

# Prints the names and hours, and sum.
def PrintNamesAndHours(names, hours):
    if len(names) != len(hours):
        print("Error: Name and Hours lists have unequal sizes.")
        return
    else:
        print("NAME","HOURS")
        i = 0
        while i < len(names):
            print(names[i],hours[i])
            i = i + 1
        print("------------------")
        print("TOTAL HOURS: ",sum(hours))

# Get hours from user
def AskForHoursWorked(employees):
    hours = []
    for emp in employees:
        hr = float(input("Enter the hours for " + emp + " : "))
        hours.append(hr)
    return hours


#######################################################################
# CONSTANTS

LIST_OF_EMPLOYEES = [
    'Jim Johnson',
    'Sam Smith',
    'Lenny Pile',
    'Lisa Penny',
    'Mary Overton',
    'Rich Richardson',
    'Irina Irinovna',
    'Karl Karlson',
    'Terry Brown',
    'Jake Natalizia'
]
#######################################################################
# MAIN PROGRAM

def main():
    print("=================================")
    print("     Employee Hours Program      ")
    print("=================================")
    print("Current Employees are: ")
    PrettyPrintNames(LIST_OF_EMPLOYEES)
    print()
    total_hours = AskForHoursWorked(LIST_OF_EMPLOYEES)
    print()
    PrintNamesAndHours(LIST_OF_EMPLOYEES, total_hours)



if __name__ == "__main__":
    main()