from IOStatements import evaluateInput, evaluatePrint
from controlStatements import evaluateIf, evaluateWhile
from expressionParser import evaluateExpression
import sys


# This function parses the token - first 'word' in each line
def evaluateTokenByToken(token, queue, variables):
	#print(token)

    # do what needs to be done according to what the token (first word) of the line is
    if token == "PRINT":
        #print("token is print")
        evaluatePrint(queue, variables)

    elif token == "INPUT":
        #print("token is input")
        evaluateInput(queue, variables)

    elif token == "IF":
        #print("token is if")
        evaluateIf(queue, variables)

    elif token == "WHILE":
        #print("token is while")
        evaluateWhile(queue, variables)

    elif token == "STOP":
        #print("token is stop")
        queue.popleft()
        print("Program terminated prematurely by \"STOP\" command")
        sys.exit()

    elif token == "END":
        #print("token is end")
        queue.popleft()
        sys.exit()

    elif any(v.name.upper() == token for v in variables):  #if token is a variable
        #print("token is variable: " + token)
        evaluateExpression(queue, variables)

    else:
        print("Error in line " + str(queue[0].number) + ": first word is not recognized")
        queue.popleft()

    # You may have to update the variables as well after the evaluations
    return variables
