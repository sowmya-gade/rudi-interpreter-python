# This file evaluates the control statements - if and while
# NOTES:
# 
# If closing bracket missing, all statements will be considered as part of the block 

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
		print("Error in line " + ifLineNumber + ": " + ifLine)
		print("Description: Keyword 'then' is missing")

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in ifLine:
		print("Error in line " + ifLineNumber + ": " + ifLine)
		print("Description: Opening bracket missing for the if condition expression")
	else:
		index1 = ifLine.index(check)
	# Check for ')'
	check = ')'
	if check not in ifLine:
		print("Error in line " + ifLineNumber + ": " + ifLine)
		print("Description: Closing bracket missing for the if condition expression")
	
	else:
		index2 = ifLine.index(check)
	# Check the order
	if index2<index1:
		print("Error in line " + ifLineNumber + ": " + ifLine)
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
		print("Error in line " + Line.number + ": " + Line.line)
		print("Description: Opening bracket missing for the if condition block")
		queue.append(Line)
	else:
		qIndex1 = 0
		
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to ifBlockQ
	check = ']'
	Line = queue.popleft()
	ifBlockQ = deque()

	bracketCount = 0 #TODO

	while (bracketCount<=0):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print("Error in line " + ifLineNumber + ": " + ifLine)
			print("Description: Closing bracket missing for or within the if condition block")
			queue.append(Line)
			return (queue,variables)
			break

		if (Line.line)=='[':
			bracketCount = bracketCount-1

		elif (Line.line)==']'
			bracketCount = bracketCount+1

		if bracketCount<=0:
			ifBlockQ.append(Line)
			Line = queue.popleft()
			
		
	# Evaluate the if block if verdict is true
	if verdict is True: 
		print ("verdict is true")
		(_,variables) = programParser.evaluateLineByLine(ifBlockQ, variables)

	# CREATE ELSE BLOCK
	# Check if else block is present
	try:
		Line = queue.popleft()
		expression = Line.line
		
		expressionUp = expression.upper()
		# check = 'END'
		# if check in expressionUp:
		#	queue.append(Line)
		#	return (queue,variables)
			
		check = 'ELSE'
		elseFlag = 0
		if (expressionUp==check):
			elseFlag = 1
			elseLineNumber = Line.number
			# Check for '['
			# Get next line of the queue
			Line = queue.popleft()
			expression = Line.line
			check = '['
			if expression!=check:
				print ("In line %d: Syntax error. Opening bracket missing for the 'else' condition block" % (Line.number))
			else:
				qIndex1 = 0

			# Search queue for ']'. Till it is found, dequeue every line and add it to elseBlockQ
			elseBlockQ = deque()
			check = ']'
			Line = queue.popleft()
			while (Line.line!= check):
				# If ']' is not found till the end, throw an error
				if ((Line.line).upper()== 'END'):
					print ("In line %d: Syntax error. Closing bracket missing for the else condition block" % elseLineNumber) 
					break
				elseBlockQ.append(Line)
				Line = queue.popleft()
			
			
		else:
			queue.append(Line)
			return (queue, variables)
			
	except IndexError:
		print ("Syntax error. 'End' is missing")
		return (queue, variables)
	
	
	if elseFlag==1 and verdict == False:
		(_,variables) = programParser.evaluateLineByLine(elseBlockQ, variables)	
	
		
	return (queue, variables)

# Evaluates the program block with the 'while' statements
def evaluateWhile(queue, variables):
	# Return the updated queue
    # You may have to update the variables as well after the evaluations

	# Get the first element of the queue
	Line = queue.popleft() 
		
	# Get the string from the tuple
	whileLine = Line.line
	whileLineNumber = Line.number

	# Convert to upper case for case insensitivity
	#whileLineUp = whileLine.upper()

	# Check that it contains 'if'
	# check = "WHILE"
	# if check not in whileLine: 
	

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in whileLine:
		print ("In line %d: Syntax error. Opening bracket missing for the while condition expression" % (Line.number))
	else:
		index1 = whileLine.index(check)
	# Check for ')'
	check = ')'
	if check not in whileLine:
		print ("In line %d: Syntax error. Closing bracket missing for the while condition expression" % (Line.number))
	else:
		index2 = whileLine.index(check)
	# Check the order
	if index2<index1:
		print ("In line %d: Syntax error. Brackets incorrect for the while condition expression" % (Line.number))


	# Get the expression between '(' and ')' 
	whileExpression = whileLine[index1+1:index2]

	# Send to expression parser to evaluate
	whileExpQ = deque([whileExpression])
	verdict = evaluateBooleanExpression(whileExpression, Line, variables)
	
	# CREATE WHILE BLOCK

	# Check for '['
	# Get next line of the queue
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print ("In line %d: Syntax error. Opening bracket missing for the while condition block" % (Line.number))
	else:
		qIndex1 = 0
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to whileBlockQ
	check = ']'
	Line = queue.popleft()
	whileBlockQ = deque()
	while (Line.line!= check):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print ("In line %d: Syntax error. Closing bracket missing for the while condition block" % (whileLineNumber)) 
			break
		whileBlockQ.append(Line)
		Line = queue.popleft()
	counter = 0 # TODO - remove later
	while verdict==True:
		(_,variables) = programParser.evaluateLineByLine(whileBlockQ, variables) 
		
		# Send to expression parser to evaluate
		whileExpQ = deque([whileExpression])
		#(evaluatedQ,variables) = evaluateExpression(whileExpQ,variables) <TODO> Uncomment later
		counter = counter+1
		if (counter == 10):
			verdict = False# evaluatedQ.popleft()	<TODO> Uncomment later

		
	return (queue, variables)
