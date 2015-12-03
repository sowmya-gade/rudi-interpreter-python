
# This file reads the file and returns all non-empty functions

import os.path
from collections import namedtuple

def parseInputFile(fileName):

    # List of program lines
    allLines = []

    if not os.path.isfile(fileName):
        print('Error: RUDI file does not exist')
        return allLines

    # Get each line in the file

    with open(fileName, encoding="utf8") as f:
        fileContent = f.readlines()

    # Flag to keep track if the line has been added to the final list
    addToPrev = [False] *len(fileContent)

    lineIdx = 0
    for lineIdx, currLine in enumerate(fileContent):

        # Remove white spaces
        currLine = currLine.strip()

        # Remove all &s in the first line
        while currLine.startswith('&') and lineIdx==1:
            print('Error in Line 1:' + currLine)
            currLine = currLine[1:]

        # if & occurs at the end of current line
        if currLine.endswith('&'):
            currLine = currLine[:-1]
            addToPrev[lineIdx] = True

        # Remove empty lines
        if not currLine:
            if addToPrev[lineIdx-1]:
                addToPrev[lineIdx] = True
            continue

        # if & occurs at the beginning of current line
        if currLine.startswith('&'):
            newLine = allLines[-1].line + ' ' + currLine[1:]
            allLines[-1] = allLines[-1]._replace(line=newLine, number=allLines[-1].number)
            continue

        # Check if the line should be added to the previous line
        if addToPrev[lineIdx-1]:
            newLine = allLines[-1].line + ' ' + currLine
            print(newLine)
            allLines[-1] = allLines[-1]._replace(line=newLine, number=allLines[-1].number)
        # Add line and line number to the final list
        else:
            Line = namedtuple('Line', 'line number')
            lineObj = Line(line=currLine, number=lineIdx+1)
            allLines.append(lineObj)

    # Check if file is empty
    if not allLines:
        print('Error: File is empty')

    # Remove comments
    allLines = removeComments(allLines)

    # Unit Test - Print program
    # for line in allLines:
    #     print(str(line.number) + ' ' + line.line)

    # Return all the lines in the program
    return allLines


# Remove comments in the program
def removeComments(allLines):

    line = []
    startIdx = []
    lengthlines = []
    lengthChars = 0
    lineIdx = -1

    updatedLines = []
    closeBracketFound = True

    # For every line in the program
    for lineIdx, currLine in enumerate(allLines):

        # For no close bracket found
        if not closeBracketFound:
            line.append(lineIdx)
            lengthChars = 1
            startIdx.append(0)

        # For each character in the line
        for charIdx in range(len(currLine.line)):

            # Still searching for the end of the comment
            if not closeBracketFound:
                lengthChars = lengthChars + 1

            # Check if the comment start is found
            if(currLine.line[charIdx:charIdx+2] == "/*"):
                closeBracketFound = False
                line.append(lineIdx)
                startIdx.append(charIdx)
                lengthChars = 1

            # Check if the comment end is found
            if(currLine.line[charIdx:charIdx+2]=="*/"):
                closeBracketFound = True
                lengthChars = lengthChars + 1
                lengthlines.append(lengthChars)

    # If no ending is found
    if not closeBracketFound:
        print("Error in line " + str(allLines[len(line)-1].number) + ": " + allLines[len(line)-1].line)
        print("Description: Closing symbol '*/' for comment block not found")

    # Erase comments from each line
    for i, lineIdx in enumerate(line):
        newLine = allLines[lineIdx].line[:startIdx[i]] + allLines[lineIdx].line[startIdx[i]+lengthlines[i]:]
        allLines[lineIdx] = allLines[lineIdx]._replace(line=newLine, number=allLines[lineIdx].number)

    # Remove empty lines from the program
    for currLine in allLines:
        if not currLine.line:
            continue
        else:
            updatedLines.append(currLine)

    # Return updated set of lines
    return updatedLines
