
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
    for currLine in fileContent:

        # Update line index
        lineIdx = lineIdx + 1

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
            lineObj = Line(line=currLine, number=lineIdx)
            allLines.append(lineObj)

    # for line in allLines:
    #     print(str(line.number) + ' ' + line.line)

    # Check if file is empty
    if not allLines:
        print('File is empty')

    # Return all the lines in the program
    return allLines
