
# This file reads the file and returns all non-empty functions

from collections import namedtuple

def parseInputFile(fileName):

    # List of program lines
    lines = namedtuple('Line', 'line number')

    # TODO: Fill up code

    # Get each line in the file
    with open(fileName) as f:
        fileContent = f.readlines()

    lineIdx = 0
    for line in fileContent:
        lineIdx = lineIdx + 1
        if (not line):
            continue
        if(line.startswith('&') and lineIdx==1):
            print('Error in Line 1:' + line)
            line = line[1:]

        if(line.startswith('&')):




    return allLines
