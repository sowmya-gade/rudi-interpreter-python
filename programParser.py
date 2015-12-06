
# This file parses the program line by line
from collections import deque
from tokenParser import evaluateTokenByToken
import re

def  evaluateLineByLine(program, variables):
    status = False
    queue = deque()

    # Place all lines in a queue
    for ln in program:
       queue.append(ln)

    # For each line, get the first token and evaluate the first token until the queue is empty
    while len(queue) > 0:
        string = queue[0].line
        token = re.split("[ =]", string)[0]
        queue[0] = queue[0]._replace(line = queue[0].line.replace(token, "", 1))
        token = token.upper()
        evaluateTokenByToken(token, queue, variables)  #this will pop the queue


    # Return status - will be changed to false if stopped prematurely
    status = True
    return status
