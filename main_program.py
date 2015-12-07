
import sys
from readFile import parseInputFile
from structureParser import parseStructure
from programParser import evaluateLineByLine

def main(argv=None):

    # Get the name of the input file from the command line
    if argv is None:
        argv = sys.argv
    # TODO: Uncomment finally
    # fileName = argv[1]
    fileName = 'inputFile1.rud'
    fileName = 'Rudi_Test_1.rud'
    
	 
    # Read from a file
    allLines = parseInputFile(fileName)

    # Check for an error
    if not allLines:
        return

    # Check for an error
    if not allLines:
        return

    # Pass through structure parser
    program, variables = parseStructure(allLines)
    if not program:
        return

    # Pass through program parser
    program, variables = evaluateLineByLine(program,variables)



    return



if __name__ == '__main__':
    sys.exit(main())
