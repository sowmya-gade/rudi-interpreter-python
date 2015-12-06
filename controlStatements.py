# This file evaluates the control statements - if and while
# NOTES:
# Sowmya: expressionParser's queue is also assumed to be a deque 
# Prof: Currently supports only control statements with '[' in next line with that as the only character in the line

from collections import namedtuple

# Evaluates the program block with the 'if' statements
def evaluateIf(queue, variables):

    # Return the updated queue
    # You may have to update the variables as well after the evaluations

	# Get the first element of the queue
	Line = queue.popleft() 
	
	# Get the string from the tuple
	ifLine = Line.line

	# Convert to upper case for case insensitivity
	ifLineUp = ifLine.upper()

	# Check that it contains 'if'
	# check = "IF"
	# if check not in ifLineUp: 
	

	# Throw an error if line doesn't have 'then'
	check = "THEN"
	if check not in ifLineUp:
		print "In line %d: Keyword 'then' is missing." % (Line.number)

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in ifLine:
		print "In line %d: Syntax error. Opening bracket missing for the if condition expression" % (Line.number)
	else:
		index1 = ifLine.index(check)
	# Check for ')'
	check = ')'
	if check not in ifLine:
		print "In line %d: Syntax error. Closing bracket missing for the if condition expression" % (Line.number)
	else:
		index2 = ifLine.index(check)
	# Check the order
	if index2<index1:
		print "In line %d: Syntax error. Brackets incorrect for the if condition expression" % (Line.number)


	# Get the expression between '(' and ')' 
	ifExpression = ifLine(index1+1:index2)

	# Send to expression parser, get
	ifExpQ = deque([ifExpression])
	evaluatedQ = evaluateExpression(ifExpQ,variables)
	verdict = evaluatedQ.popleft()

	
	# CREATE IF BLOCK

	# Check for '['
	# Get next line of the queue
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print "In line %d: Syntax error. Opening bracket missing for the if condition block" % (Line.number)
	else:
		qIndex1 = 0
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to ifBlockQ
	check = ']'
	Line = queue.popleft()
	while (Line.line!= check):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print "In line %d: Syntax error. Closing bracket missing for the if condition block" % (Line.number)-1 #<TODO> Fix line number
			break
		ifBlockQ.append(Line)
		Line = queue.popleft()

	# CREATE ELSE BLOCK
	# Check if else block is present
	Line = queue.popleft()
	expression = Line.line
	check = 'ELSE'
	elseFlag = 0

	if (expression==check)
		elseFlag = 1
		# Check for '['
		# Get next line of the queue
		Line = queue.popleft()
		expression = Line.line
		check = '['
		if expression!=check:
			print "In line %d: Syntax error. Opening bracket missing for the 'else' condition block" % (Line.number)
		else:
			qIndex1 = 0

		# Search queue for ']'. Till it is found, dequeue every line and add it to elseBlockQ
		check = ']'
		Line = queue.popleft()
		while (Line.line!= check):
			# If ']' is not found till the end, throw an error
			if ((Line.line).upper()== 'END'):
				print "In line %d: Syntax error. Closing bracket missing for the else condition block" % (Line.number)-1 #<TODO> Fix line number
				break
			elseBlockQ.append(Line)
			Line = queue.popleft()
	
	# Evaluate the if block if verdict is true
	if verdict is True: 
		evaluateLineByLine(ifBlockQ, variables)
	else if elseFlag==1
		evaluateLineByLine(elseBlockQ, variables)
	
	
	
	# Get the lines between '[' and ']' and send to. Throw error if brackets not present
	

    return queue, variables


# Evaluates the program block with the 'while' statements
def evaluateWhile(queue, variables):

    # Return the updated queue
    # You may have to update the variables as well after the evaluations

	# Get the first element of the queue
	Line = queue.popleft() #<TODO> Verify
	
	# Get the string from the tuple
	whileLine = Line.line

	# Convert to upper case for case insensitivity
	whileLine = whileLine.upper()

	# Check that it contains 'if'
	check = "WHILE"
	if check not in whileLine: #<TODO> How should I indicate this internal error 
	

	# Throw an error if line doesn't have '(' followed by ')'
	# Check for '('
	check = '('
	if check not in whileLine:
		print "In line %d: Syntax error. Opening bracket missing for the while condition expression" % (Line.number)
	else:
		index1 = whileLine.index(check)
	# Check for ')'
	check = ')'
	if check not in whileLine:
		print "In line %d: Syntax error. Closing bracket missing for the while condition expression" % (Line.number)
	else:
		index2 = whileLine.index(check)
	# Check the order
	if index2<index1:
		print "In line %d: Syntax error. Brackets incorrect for the while condition expression" % (Line.number)


	# Get the expression between '(' and ')' 
	whileExpression = whileLine(index1+1:index2)

	# Send to expression parser to evaluate
	whileExpQ = deque([whileExpression])
	evaluatedQ = evaluateExpression(whileExpQ,variables)
	verdict = evaluatedQ.popleft()

	# CREATE WHILE BLOCK

	# Check for '['
	# Get next line of the queue
	Line = queue.popleft()
	expression = Line.line
	check = '['
	if expression!=check:
		print "In line %d: Syntax error. Opening bracket missing for the while condition block" % (Line.number)
	else:
		qIndex1 = 0
	
	# Search queue for ']'. Till it is found, dequeue every line and add it to ifBlockQ
	check = ']'
	Line = queue.popleft()
	while (Line.line!= check):
		# If ']' is not found till the end, throw an error
		if ((Line.line).upper()== 'END'):
			print "In line %d: Syntax error. Closing bracket missing for the while condition block" % (Line.number)-1 #<TODO> Fix line number
			break
		whileBlockQ.append(Line)
		Line = queue.popleft()

	while verdict==True
		(status,variables) = evaluateLineByLine(whileBlockQ, variables) # <TODO> - check syntax to take multiple outputs
		if status == False # TODO - should I print anything or will programParser print. Probably should still print

		# Send to expression parser to evaluate
		whileExpQ = deque([whileExpression])
		(evaluatedQ,variables) = evaluateExpression(whileExpQ,variables) # <TODO> - check syntax to take multiple outputs
		verdict = evaluatedQ.popleft()	


    return queue, variables
