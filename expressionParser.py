# This file evaluates assignment statements and calculates expressions


from collections import deque
from collections import namedtuple

# Parse the expression line of the program
def evaluateExpression(queue, variables):

    currLine = queue.popleft()

    equation = currLine.line.split("=")

    # No assignment equation
    if len(equation) == 1:
        print("Error in line " + str(currLine.number) + ": " + currLine.line)
        print("Description: Invalid assignment found for the token \"" + currLine.line + "\"")
        return queue, variables

    # More than one assignment
    elif len(equation) > 2:
        print("Error in line " + str(currLine.number) + ": " + currLine.line)
        print("Description: Only single '=' allowed in an expression")
        return queue, variables

    # LHS and RHS are found
    else:
        lhs = equation[0].strip()
        rhs = equation[1].split()

        # Check for a single variable on the left hand side
        if not len(lhs) == 1:
            print("Error in line " + str(currLine.number) + ": " + currLine.line)
            print("Description: Invalid assignment expression")
            return queue, variables

        # Find the variable in the list of variables
        variableFound = False
        lhsVariableIdx = -1
        for i in range(len(variables)):
            if lhs.upper() == variables[i].name:
                lhsVariableIdx = i
                variableFound = True
                break

        # Check for an error
        if not variableFound:
            print("Error in line " + str(currLine.number) + ": " + currLine.line)
            print("Description: Variable \"" + lhs + "\" does not exist")
            return queue, variables

        # Check if variable is of string type
        if variables[lhsVariableIdx].type == "STRING":

            # Get the rhs value
            rhs = equation[1].strip()

            # Check if the initialization is with a variable
            for i in range(len(variables)):
                if rhs.upper() == variables[i].name:

                    # Check if the variable is not of string type
                    if variables[i].type == "INTEGER" and variables[i].type == "FLOAT":
                        print("Error in line " + str(currLine.number) + ": " + currLine.line)
                        print("Description: Invalid variable \"" + variables[i].name + "\" cannot be used to initialize variable of string type")
                        return queue, variables

                    # If the variable has a value field
                    elif variables[i].value:
                        value = variables[i].value
                        variables[lhsVariableIdx] = variables[lhsVariableIdx]._replace (name=variables[lhsVariableIdx].name,value=value,type=variables[lhsVariableIdx].type)
                        return queue, variables

                    # Uninitialized value is found
                    else:
                        print("Error in line " + str(currLine.number) + ": " + currLine.line)
                        print("Description: \"" + variables[i].name + "\" has not been initialized with a value")
                        return queue, variables

            # Check for quotes
            if rhs[0]=="\"" and rhs[-1]=="\"":
                variables[lhsVariableIdx] = variables[lhsVariableIdx]._replace (name=variables[lhsVariableIdx].name,value=rhs,type=variables[lhsVariableIdx].type)
                return queue, variables

            # Invalid initialization error
            else:
                print("Error in line " + str(currLine.number) + ": " + currLine.line)
                print("Description: Invalid initialization \""+ rhs +"\" for variable of type string ")
                return queue, variables

        # RHS is an equation
        else:

            # Check if all elements of rhs are valid
            for idx, token in enumerate(rhs):

                # Check if the token is a variable
                variableFound = False
                for i in range(len(variables)):
                    if token.upper() == variables[i].name:

                        # Check if the variable is not of string type
                        if variables[i].type == "STRING":
                            print("Error in line " + str(currLine.number) + ": " + currLine.line)
                            print("Description: Invalid variable \"" + token + "\" of string type present in the equation")
                            return queue, variables

                        # If the variable has a value field
                        elif variables[i].value:
                            rhs[idx] = variables[i].value
                            variableFound = True
                            break

                        # Uninitialized value is found
                        else:
                            print("Error in line " + str(currLine.number) + ": " + currLine.line)
                            print("Description: \"" + token + "\" has not been initialized with a value")
                            return queue, variables

                # Check if the token is a number
                if variableFound:
                    continue

                # Check if the token is a number
                elif isfloat(token):
                    continue

                # Check if the token is a '+'
                elif token == "+":
                    continue

                # Check if the token is a '-'
                elif token == "-":
                    continue

                # Check if the token is a '/'
                elif token == "/":
                    continue

                # Check if the token is a '*'
                elif token == "*":
                    continue

                # Check if the token is a '('
                elif token == "(":
                    continue

                # Check if the token is a ')'
                elif token == ")":
                    continue

                # Invalid Token Error
                else:
                    print("Error in line " + str(currLine.number) + ": " + currLine.line)
                    print("Description: \"" + token + "\" is an invalid token")
                    return queue, variables

            # Convert the infix RHS expression to postfix notation
            postfixExpr = infixToPostfix(rhs)

            # Check for valid conversion
            if not postfixExpr:
                print("Error in line " + str(currLine.number) + ": " + currLine.line)
                print("Description: Invalid element found in the expression")
                return queue, variables

            # Evaluate the postfix expression
            error, value = evaluatePostfix(postfixExpr, currLine)

            # Check for an error
            if error:
                return queue, variables

            # Update the value of the variable with the calculated value
            else:
                # Perform type conversion for int variables
                if variables[lhsVariableIdx].type == "INTEGER":
                    value = int(value)

                # Update value of variable
                variables[lhsVariableIdx] = variables[lhsVariableIdx]._replace(name=variables[lhsVariableIdx].name, value=value, type=variables[lhsVariableIdx].type)


    # Return the updated queue and variables
    return queue, variables



# Converts an infix expression to a postfix expression
def infixToPostfix(infixExpression):

    # Create a dictionary of the precedence
    precedence = {}
    precedence["*"] = 5
    precedence["/"] = 4
    precedence["+"] = 3
    precedence["-"] = 2
    precedence["("] = 1

    # Stack for the operators
    opStack = deque()

    # Postfix Expresssion list
    postfixExpr = []

    # Error flag
    error = False

    # Go through each token in the list
    for token in infixExpression:

        # Check if token is valid - int or float
        if isint(token) or isfloat(token):
            postfixExpr.append(token)

        # Push token onto the stack if it is an open bracket
        elif token == '(':
            opStack.append(token)

        # Pop token from the stack if it is an close bracket
        elif token == ')':
            topToken = opStack.pop()

            # Add to the postfix list till an open bracket is found in the stack
            while topToken != '(':
                postfixExpr.append(topToken)
                if opStack:
                    topToken = opStack.pop()
                else:
                    error = True
                    break

            # Break the loop if there is an error
            if error:
                break

        # Check if the token is an operator
        elif token == '*' or token == '/' or token == '+' or token == '-':

            # If the stack is not empty
            if opStack:
                # Pop operators till a lower precedence operator is encountered in the stack
                while opStack and (precedence[opStack[-1]] >= precedence[token]):
                      postfixExpr.append(opStack.pop())

            # Add the operator to the stack
            opStack.append(token)

        # Else - Invalid token found
        else:
            print("Description: Invalid element found in the expression")
            error = True
            break

    # Check for no error
    if not error:

        # Append all remaining operators in the stack
        while opStack:
            postfixExpr.append(opStack.pop())

        # Return the postfix expression
        return postfixExpr

    # Return an empty list if an error is encountered
    else:
        return []


# Evaluate the postfix Expression
def  evaluatePostfix(postfixExpr, currLine):

    # Create Stack - for the the operands
    operandStack = deque()

    # Error flag
    error = False

    # Go through each token
    for token in postfixExpr:

        # Check if token is a value
        if isint(token) or isfloat(token):

            # Push onto the stack
            operandStack.append(float(token))

        # Pop to operands from the stack
        else:
            if len(operandStack) > 1:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()

                # Perform the operation
                error, result = performOperation(token,operand1,operand2)
                if error:
                    print("Error in line " + str(currLine.number) + ": " + currLine.line)
                    print("Description: Incorrect operator \"" + token + "\"")
                    break

                # Push the result onto the stack
                operandStack.append(result)
            else:
                print("Error in line " + str(currLine.number) + ": " + currLine.line)
                print("Description: Incorrect equation")
                error = True
                break

    # Return the appropriate value
    if error:
        return error, -1
    elif len(operandStack) == 1:
        # Return the last value in the stack
        return error, operandStack.pop()
    else:
        print("Error in line " + str(currLine.number) + ": " + currLine.line)
        print("Description: Incorrect equation")
        error = True
        return error, -1

# Performs operation (operator) on the two operands
def performOperation(operator, operand1, operand2):

    # Error flag
    error = False

    # Check for multiplication
    if operator == "*":
        return error, operand1 * operand2

    # Check for division
    elif operator == "/":
        return error, operand1 / operand2

    # Check for addition
    elif operator == "+":
        return error, operand1 + operand2

    # Check for subtraction
    elif operator == "-":
        return error, operand1 - operand2

    else:
        error = True
        return error, operand1

# Check is a string is float
def  isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

# Check if a string is int
def  isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

# Computes a value given an expression
def  doMath(expression, currLine, variables):

    error = False
    expression = expression.strip()

    # Check for raw string
    if expression.startswith('"') and expression.endswith('"'):
        return error, expression

    # Check for string variable
    expression = expression.split()
    if(len(expression) == 1):
        for i in range(len(variables)):
            if expression[0].upper() == variables[i].name:

                # Check if the variable is of string type
                if variables[i].type == "STRING":

                    # If the variable has a value field
                    if variables[i].value:
                        return error, variables[i].value

                    # Uninitialized value is found
                    else:
                        error = True
                        print("Error in line " + str(currLine.number) + ": " + currLine.line)
                        print("Description: \"" + variables[i].name + "\" has not been initialized with a value")
                        return error, -1

    # Check if all elements of expression are valid
    for idx, token in enumerate(expression):

        # Check if the token is a variable
        variableFound = False
        for i in range(len(variables)):
            if token.upper() == variables[i].name:

                # Check if the variable is not of string type
                if variables[i].type == "STRING":
                    error = True
                    print("Error in line " + str(currLine.number) + ": " + currLine.line)
                    print("Description: Invalid variable \"" + token + "\" of string type present in the equation")
                    return error, -1

                # If the variable has a value field
                elif variables[i].value:
                    expression[idx] = variables[i].value
                    variableFound = True
                    break

                # Uninitialized value is found
                else:
                    error = True
                    print("Error in line " + str(currLine.number) + ": " + currLine.line)
                    print("Description: \"" + token + "\" has not been initialized with a value")
                    return error, -1

        # Check if the token is a number
        if variableFound:
            continue

        # Check if the token is a number
        elif isfloat(token):
            continue

        # Check if the token is a '+'
        elif token == "+":
            continue

        # Check if the token is a '-'
        elif token == "-":
            continue

        # Check if the token is a '/'
        elif token == "/":
            continue

        # Check if the token is a '*'
        elif token == "*":
            continue

        # Check if the token is a '('
        elif token == "(":
            continue

        # Check if the token is a ')'
        elif token == ")":
            continue

        # Invalid Token Error
        else:
            error = True
            print("Error in line " + str(currLine.number) + ": " + currLine.line)
            print("Description: \"" + token + "\" is an invalid token")
            return error, -1

    # Convert the infix RHS expression to postfix notation
    postfixExpr = infixToPostfix(expression)

    # Check for valid conversion
    if not postfixExpr:
        error = True
        print("Error in line " + str(currLine.number) + ": " + currLine.line)
        print("Description: Invalid element found in the expression")
        return error, -1
    print(expression)
    print(postfixExpr)
    # Evaluate the postfix expression
    error, value = evaluatePostfix(postfixExpr, currLine)

    # Check for an error
    if error:
        return error, -1

    return error, value