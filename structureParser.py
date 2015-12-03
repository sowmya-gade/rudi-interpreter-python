
# This file checks for structure errors and finds the variables and
# the program block.


from collections import namedtuple

def  parseStructure(allLines):

    # List of variables
    variables = []

    # Each variable is defined with - name, value and type
    variable = namedtuple('Variable', 'name value type')

    # List of lines in the program block
    program = []

    # Each line is defined with - line and number
    #line = namedtuple('Line', 'line number')

    #TODO: Fill up with code

    # Check for the program keyword
    if(allLines[0].line.lower()!="program"):
        print("Error in line 1: " + allLines[0].line)
        print("Description: Keyword 'program' missing in the beginning of the the program")

    # Check for decs
    # for line in allLines:

    # Check for begin


    # Check for end

    return program, variables