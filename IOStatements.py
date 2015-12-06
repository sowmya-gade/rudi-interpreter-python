# This file evaluates the IO statements


# This function evaluates the 'print' statement
def evaluatePrint(queue, variables):

    tempLine = queue.popleft()
    string = tempLine.line.strip()  #removes whitespace at ends of string
    firstWord = string.split(" ", 1)[0]
    firstWord = firstWord.strip()

    if string.startswith('"') and string.endswith('"'):  #if a statement in quotes
        string2 = string[string.index('"')+1:string.rindex('"')]
        print(string2)
        if len(string) != len(string2)+2:
            print("Error in line " + str(tempLine.number) + ": characters outside of quotes in print statement")

    elif firstWord.upper() == "CR":  #if first word is "cr" (case insensitive)
        print("")
        if len(string) != 2:
            print("Error in line " + str(tempLine.number) + ": extra characters after \"cr\" command in print statement")


    elif any(v.name == firstWord.upper() for v in variables):  #test if firstWord it is a variable (case insensitive)
        for v in variables:
            if v.name == firstWord.upper():
                print(v.value)
        if len(string) != len(firstWord):
            print("Error in line " + str(tempLine.number) + ": extra characters after variable in print statement")

    else:
         print("Error in line " + str(tempLine.number) + ": print statement incorrect")

    # Return the updated queue
    return queue



# This function evaluates the 'input' statement
def evaluateInput(queue, variables):
    tempLine = queue.popleft()
    string = tempLine.line.strip()  #removes whitespace at ends of string
    firstWord = string.split(" ", 1)[0]
    firstWord = firstWord.strip()

    if any(v.name == firstWord.upper() for v in variables):  #test if firstWord it is a variable (case insensitive)
        for i in range(0, len(variables)):
            if variables[i].name == firstWord.upper():
                while True:
                    val = input("Enter new value for variable " + variables[i].name + ": ")
                    if variables[i].type == "integer":
                        try:
                            val = int(eval(val))
                            variables[i] = variables[i]._replace(value = val)
                            break
                        except:
                            print("Error, input cannot be cast as an integer.")
                    elif variables[i].type == "float":
                        try:
                            val = float(eval(val))
                            variables[i] = variables[i]._replace(value = val)
                            break
                        except:
                            print("Error, input cannot be cast as a float.")
                    elif variables[i].type == "string":
                            variables[i] = variables[i]._replace(value = val)  #incoming value is already a string
                            break
                    else:
                        print("Error in variables. " + variables[i].name + " variable data type stored incorrectly") # in case variables list is corrupted
                        break
        if len(string) != len(firstWord):
            print("Error in line " + str(tempLine.number) + ": extra characters after variable in input statement.")
    else:
        print("Error in line " + str(tempLine.number) + ": variable was not declared")

    # Return the updated queue and variables
    return queue, variables