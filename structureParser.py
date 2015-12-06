
# This file checks for structure errors and finds the variables and
# the program block.

from collections import namedtuple

def  parseStructure(allLines):

    # Check for the program keyword
    checkForProgram(allLines)

    # Check for decs
    variables = checkForDecs(allLines)

    # Check for end
    allLines = checkForEnd(allLines)

    # Get the program block
    program = getProgram(allLines)

    # Unit Test - Print variables
    for variable in variables:
        print(variable.type + ' ' + variable.name)

    # Unit Test - Print variables
    for line in program:
        print(str(line.number) + ' ' + line.line)

    # Check if there are no lines in the program
    if not program:
        print("Error: No lines in the program")

    return program, variables


# Check for the program keyword
def checkForProgram(allLines):

    if(allLines[0].line.lower()!="program"):
        print("Error in line 1: " + allLines[0].line)
        print("Description: Keyword 'program' missing at the beginning of the the program")

    return


# Check for the declarations
def  checkForDecs(allLines):

    # List of variables
    variables = []

    # Each variable is defined with - name, value and type
    Variable = namedtuple('Variable', 'name value type')

    # Check for decs
    decsLine = -1
    foundDecs = False
    foundOpenBracket = False
    noBrackets = False
    for idx, currLine in enumerate(allLines):

        # Split the line with a ' ' demlimiter
        words = currLine.line.strip().split()

        # Check if the keyword is found and the close bracket is not found
        if foundDecs and not foundOpenBracket:
            if words[0] == '[':
                foundOpenBracket = True
                decsLine = idx + 1
                if len(words)>1:
                    print("Error in line " + str(currLine.number) + ": " + currLine.line)
                    print("Description: Unidentified additional characters found in the line")
                break

        #Check if no brackets follow
        if foundDecs:
            decsLine = idx + 1
            noBrackets = True
            break

        # Find the 'decs' keyword
        if words[0].lower()=='decs':
            foundDecs  = True
            if (len(words)>1):
                if words[1] == '[':
                    foundOpenBracket = True
                    decsLine = idx + 1
                    if len(words)>2:
                        print("Error in line " + str(currLine.number) + ": " + currLine.line)
                        print("Description: Unidentified additional characters found in the line")
                    break

    # Error if no brackets are found for decs
    if foundDecs and noBrackets:
        print("Error in line " + str(allLines[decsLine-1].number) + ": " + allLines[decsLine-1].line)
        print("Description: Missing opening brackets for decs")

    # Retrieve the declarations
    foundCloseBracket = False
    if foundDecs and foundOpenBracket and not noBrackets:

        # Get all variables
        for i in range(decsLine,len(allLines)):

            # Close bracket is found
            if allLines[i].line == ']':
                foundCloseBracket = True
                break

            # Split line according to ' '
            words = allLines[i].line.strip().split(' ')

            # If insufficient information is found
            if len(words) < 2:
                print("Error in line " + str(allLines[i].number) + ": " + allLines[i].line)
                print("Description: Insufficient information for the variable")
                continue

            # Check for type of declaration
            if words[0].upper() == "INTEGER":
                type = 'INTEGER'
            elif words[0].upper() == "FLOAT":
                type = 'FLOAT'
            elif words[0].upper() == "STRING":
                type = 'STRING'
            else:
                print("Error in line " + str(allLines[i].number) + ": " + allLines[i].line)
                print("Description: Unidentified variable type")
                continue

            # Get variable name
            name = words[1].upper()

            # Add the variable to the list
            variables.append(Variable(name=name, value='', type=type))

            # If extra information is found
            if len(words) > 2:
                print("Error in line " + str(allLines[i].number) + ": " + allLines[i].line)
                print("Description: Unidentified additional characters found in the line")
                continue

    # Error if no brackets are found for decs
    if noBrackets:
        print("Error in line " + str(allLines[decsLine-1].number) + ": " + allLines[decsLine-1].line)
        print("Description: Missing brackets for decs")

    # Error if close bracket is not found
    if foundOpenBracket and not foundCloseBracket:
        print("Error in line " + str(allLines[decsLine-1].number) + ": " + allLines[decsLine-1].line)
        print("Description: Missing corresponding close bracket")

    return variables


# Check for an ending for the program
def  checkForEnd(allLines):

    Line = namedtuple('Line', 'line number')

    if not allLines[-1].line.lower() == "end":
        print("Error in line " + str(allLines[-1].number) + ": " + allLines[-1].line)
        print("Description: No 'end' found for the program")
        allLines.append(Line(line="end", number=allLines[-1].number+1))

    return allLines


# Get the program block of the program
def  getProgram(allLines):

    program = []
    foundBegin = False

    # Go through each line
    for line in allLines:

        # Get the current line
        currLine = line.line.strip()

        # Loop till the end is found
        if currLine.lower() == "end":
            program.append(line)
            break

        # Find the keyword - begin
        if currLine.lower() == "begin":
            foundBegin = True
            continue

        # Get the program lines
        if foundBegin:
            program.append(line)

    # Error if keyword 'begin' is not found
    if not foundBegin:
        print("Error: 'begin' for program not found")

    return program