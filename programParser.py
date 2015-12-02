
# This file parses the program line by line

import controlStatements as control
import expressionParser as expression
import IOStatements as io
import tokenParser as token

def  evaluateLineByLine(program, variables):

    # Place all lines in a queue

    # For each line, get the first token

    # Evaluate the first token - till the queue is empty

    # Return status - will be changed to false if stopped prematurely
    status = True

    return status