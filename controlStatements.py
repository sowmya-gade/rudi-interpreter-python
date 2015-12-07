# This file evaluates the control statements - if and while
# NOTES:
# Sowmya: expressionParser's queue is also assumed to be a deque 
# Prof: Currently supports only control statements with '[' in next line with that as the only character in the line
# If closing bracket missing, all statements will be considered as part of the black and error line number will be last line

from collections import namedtuple
from collections import deque

from expressionParser import evaluateExpression
import programParser

# Evaluates the program block with the 'if' statements
def evaluateIf(queue, variables):
	print ("I am the mighty IfEvaluator. Why did you call me?")
    # Return the updated queue
    # You may have to update the variables as well after the evaluations

	# Get the first element of the queue
	Line = queue.popleft() 
	
	# Get the string from the tuple
	ifLine = Line.line
	print ("ifLine: %s" %ifLine)
	ifLineNumber = ifLine.number

	# Convert to upper case for case insensitivity
	ifLineUp = ifLine.upper()

	# Check that it contains 'if'
	# check = "IF"
	# if check not in ifLineUp: 
	

	# Throw an error if line doesn't have 'then'
	check = "THEN"
	if check not in ifLineUp:
		print ("In line %d: Keyword 'then' is missing." % (Line.number))

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in ifLine:
		print ("In line %d: Syntax error. Opening bracket missing for the if condition expression" % (Line.number))
	else:
		index1 = ifLine.index(check)
	# Check for ')'
	check = ')'
	if check not in ifLine:
		print ("In line %d: Syntax error. Closing bracket missing for the if condition expression" % (Line.number))
	else:
		index2 = ifLine.index(check)
	# Check the order
	if index2<index1:
		print ("In line %d: Syntax error. Brackets incorrect for the if condition expression" % (Line.number))


	# Get the expression between '(' and ')' 
	ifExpression = ifLine[index1+1:index2]
	print ("ifExpression: %s" %ifExpression)

	# Send to expression parser, get
	ifExpQ = deque([ifExpression])
	# evaluatedQ = evaluateExpression(ifExpQ,variables) <TODO> Uncomment later
	verdict = False #evaluatedQ.popleft() <TODO> Uncomment later

	
	# CREATE IF BLOCK

	# Check for '['
	# Get next line of the queue
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print ("In line %d: Syntax error. Opening bracket missing for the if condition block" % (Line.number))
		queue.append(Line)
	else:
		qIndex1 = 0
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to ifBlockQ
	check = ']'
	Line = queue.popleft()
	ifBlockQ = deque()
	while (Line.line!= check):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print ("In line %d: Syntax error. Closing bracket missing for the if condition block" % ifLineNumber)
			queue.append(Line)
			return (queue,variables)
			break
		
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
	print ("I am the mighty whileEvaluator. Why did you call me?")
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
	#evaluatedQ = evaluateExpression(whileExpQ,variables) <TODO> Uncomment later
	verdict = True#evaluatedQ.popleft() <TODO> Uncomment later

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
