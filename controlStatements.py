# This file evaluates the control statements - if and while
# NOTES:
# If closing bracket is missing, all statements will be considered as part of the block 

from collections import namedtuple
from collections import deque

from expressionParser import evaluateExpression
import programParser
from evaluateBexpression import evaluateBooleanExpression

# Evaluates the program block with the 'if' statements
def evaluateIf(queue, variables):
	# IF LINE SYNTAX CHECK
	# Get the first element of the queue
	Line = queue.popleft() 
	
	# Get the string from the tuple
	ifLine = Line.line
	ifLineNumber = Line.number

	# Convert to upper case for case insensitivity
	ifLineUp = ifLine.upper()

	# Throw an error if line doesn't have 'then'
	check = "THEN"
	if check not in ifLineUp:
		print("Error in line " + str(ifLineNumber) + ": " + ifLine)
		print("Description: Keyword 'then' is missing")

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in ifLine:
		print("Error in line " + str(ifLineNumber) + ": " + ifLine)
		print("Description: Opening bracket missing for the if condition expression")
	else:
		index1 = ifLine.index(check)
	# Check for ')'
	check = ')'
	if check not in ifLine:
		print("Error in line " + str(ifLineNumber) + ": " + ifLine)
		print("Description: Closing bracket missing for the if condition expression")
	
	else:
		index2 = ifLine.index(check)
	# Check the order
	if index2<index1:
		print("Error in line " + str((ifLineNumber) + ": " + ifLine)
		print("Description: Brackets incorrect for the if condition expression")
	

	# Get the expression between '(' and ')' 
	ifExpression = ifLine[index1+1:index2]
	
	# Send the expression to the boolean expression evaluator
	verdict = evaluateBooleanExpression(ifExpression,Line,variables)

	# Check for any other garbage
	# <TODO> string.replace

	
	# CREATE IF BLOCK	
	# Check for '['
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print("Error in line " + str(Line.number) + ": " + Line.line)
		print("Description: Opening bracket missing for the if condition block")
		queue.append(Line)
	else:
		qIndex1 = 0
		
	
	# Search queue for ']'. Till the closing bracket of if block is found, dequeue every line and add it to ifBlockQ
	check = ']'
	Line = queue.popleft()
	ifBlockQ = deque()

	bracketCount = 0 # To keep track of nested loops

	while (bracketCount<=0):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print("Error in line " + str(ifLineNumber) + ": " + ifLine)
			print("Description: Closing bracket missing for or within the if condition block")
			queue.append(Line)
			return (queue,variables)
			break

		# Keep track of number of opening and closing brackets. Since if block's opening bracket was already checked outside the loop,
		# the number of closing brackets will be 1 greater than the opening brackets. So when the count becomes 1, if block's closing
		# bracket has been found
		if (Line.line)=='[':
			bracketCount = bracketCount-1

		elif (Line.line)==']':
			bracketCount = bracketCount+1

		# once the closing bracket is found, do not add it to the if block queue and do not pop the program queue  
		if bracketCount<=0:
			ifBlockQ.append(Line)
			Line = queue.popleft()
			
		
	# Evaluate the if block if verdict is true
	if verdict is True: 
		(_,variables) = programParser.evaluateLineByLine(ifBlockQ, variables)

	# CREATE ELSE BLOCK
	Line = queue.popleft()
	elseLine = Line.line		
	elseLineUp = elseLine.upper()

	# Check if the next line is an 'end' and return if so
	check = 'END'
	if check in elseLineUp:
		queue.append(Line)
		return (queue,variables)

	# Check if the next line is an 'else'
	check = 'ELSE'
	elseFlag = 0
	if (elseLineUp==check):
		elseFlag = 1
		elseLineNumber = Line.number

		
		
		# Check for '['
		# Get next line of the queue
		Line = queue.popleft()
		expression = Line.line
		check = '['
		if expression!=check:
			print("Error in line " + str(Line.number) + ": " + expression)
			print("Description: Opening bracket missing for the else condition block")
		else:
			qIndex1 = 0

	
		# Search queue for ']'. Till it is found, dequeue every line and add it to elseBlockQ
		check = ']'
		elseBlockQ = deque()
		Line = queue.popleft()		

		bracketCount = 0 # To keep track of nested loops
		while (bracketCount<=0 ):
			# If ']' is not found till the end, throw an error
			if ((Line.line).upper()== 'END'):
				print("Error in line " + str(elseLineNumber) + ": " + elseLine)
				print("Description: Closing bracket missing for or within the else condition block")
				queue.append(Line)
				return (queue,variables)
			

			# Keep track of number of opening and closing brackets. Since else block's opening bracket was already checked outside the loop,
			# the number of closing brackets will be 1 greater than the opening brackets. So when the count becomes 1, else block's closing
			# bracket has been found
			if (Line.line)=='[':
				bracketCount = bracketCount-1

			elif (Line.line)==']':
				bracketCount = bracketCount+1

			# once the closing bracket is found, do not add it to the else block queue and do not pop the program queue  
			if bracketCount<=0:
				elseBlockQ.append(Line)
				Line = queue.popleft()

			
	# if 'else' not present append line back to queue and return
	else:
		queue.append(Line)
		return (queue, variables)
			

	
	if elseFlag==1 and verdict == False:
		(_,variables) = programParser.evaluateLineByLine(elseBlockQ, variables)	
	
		
	return (queue, variables)

# Evaluates the program block with the 'while' statements
def evaluateWhile(queue, variables):
	
	# Get the first element of the queue
	Line = queue.popleft() 
		
	# Get the string from the tuple
	whileLine = Line.line
	whileLineNumber = Line.number
	
	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in whileLine:
		print("Error in line " + str(whileLineNumber) + ": " + whileLine)
		print("Description: Opening bracket missing for the while condition expression")
	else:
		index1 = whileLine.index(check)
	# Check for ')'
	check = ')'
	if check not in whileLine:
		print("Error in line " + str(whileLineNumber) + ": " + whileLine)
		print("Description: Closing bracket missing for the while condition expression")
	else:
		index2 = whileLine.index(check)
	# Check the order
	if index2<index1:
		print("Error in line " + str(whileLineNumber) + ": " + whileLine)
		print("Description: Brackets incorrect for the while condition expression")


	# Get the expression between '(' and ')' 
	whileExpression = whileLine[index1+1:index2]

	# Send to expression parser to evaluate
	# whileExpQ = deque([whileExpression])
	verdict = evaluateBooleanExpression(whileExpression, Line, variables)
	
	# CREATE WHILE BLOCK

	# Check for '['
	# Get next line of the queue
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print ("In line %d: Syntax error. Opening bracket missing for the while condition block" % (Line.number))
		print("Error in line " + str(Line.number) + ": " + Line)
		print("Description: Opening bracket missing for the while condition block")		
	else:
		qIndex1 = 0
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to whileBlockQ
	check = ']'
	Line = queue.popleft()
	whileBlockQ = deque()

	bracketCount = 0 # To keep track of nested loops
	while (bracketCount <= 0):
		# If ']' is not found till the end, throw an error
		
		if ((Line.line).upper()== 'END'):
			print("Error in line " + str(whileLineNumber) + ": " + whileLine)
			print("Description: Closing bracket missing for or within the while condition block")
			queue.append(Line)
			return (queue,variables)
			
		
		# Keep track of number of opening and closing brackets. Since else block's opening bracket was already checked outside the loop,
		# the number of closing brackets will be 1 greater than the opening brackets. So when the count becomes 1, else block's closing
		# bracket has been found
		if (Line.line)=='[':
			bracketCount = bracketCount-1

		elif (Line.line)==']':
			bracketCount = bracketCount+1

		# once the closing bracket is found, do not add it to the else block queue and do not pop the program queue  
		if bracketCount<=0:
			whileBlockQ.append(Line)
			Line = queue.popleft()

		

	# Evaluate the verdict and run the while loop while it evaluates to true
	verdict = evaluateBooleanExpression(whileExpression, Line, variables)
	while verdict==True:
		(_,variables) = programParser.evaluateLineByLine(whileBlockQ, variables) 
		
		# Update verdict
		verdict = evaluateBooleanExpression(whileExpression, Line, variables) 
		
		
	return (queue, variables)
