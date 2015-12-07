from collections import namedtuple

def evaluateBooleanExpression (expression, Line, variables):
	# Split by OR
	expsOR = expression.split("|")

	valueList = []
	# Call 'evaluateAfterOR' for each element of the expsOR list and append the result to 'valueList'
	for eachExp in expsOR:
		(value,errorFlag) = evaluateAfterOR(eachExp,Line,variables)
		if (errorFlag == 1):
			return 0
		else:	
			valueList.append(value)
		
	# Perform OR between elements of the valueList (even when list has only one element) 
	for value in valueList:
		if value != 0:
			return 1
	return 0	

def evaluateAfterOR (exp,Line,variables):
	# Split by AND
	expsAND = exp.split("^") 

	valueList = []
	# Call 'evaluateAfterAND' for each element of the expsAND list and append the result to 'valueList'
	for eachExp in expsAND:
		(value,errorFlag) = evaluateAfterAND(eachExp,Line,variables)
		if (errorFlag == 1):
			return 0, 1
		else:	
			valueList.append(value)

	# Perform AND between elements of valueList (even when list has only one element) 
	for value in valueList:
		if value == 0:
			return 0, errorFlag
	return 1, errorFlag

	
def evaluateAfterAND (exp,Line,variables):
	# Check for each possible comparison operator. Check for not operator and send the LHS and RHS to doMath. Throw error if less than 1 or greater than 2 components
	valueList = []
	counter = 0
	if ":eq:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":eq:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]==valueList[1]:
					result = 1
				else:
					result = 0					
			
	
	if ":ne:" in exp:
		counter = counter+1
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":ne:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]!=valueList[1]:
					result = 1
				else:
					result = 0
					
	if ":gt:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":gt:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]>valueList[1]:
					result = 1
				else:
					result = 0
					
	if ":lt:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":lt:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]<valueList[1]:
					result = 1
				else:
					result = 0
					
	if ":ge:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":ge:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]>=valueList[1]:
					result = 1
				else:
					result = 0
					
	if ":le:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression\"" + exp + "\"")
			return 0,1
		else:
			exps = exp.splits(":le:")
			for eachExp in exps:
				(value,errorFlag) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					valueList.append(value)
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression\"" + exp + "\"")
				return 0,1
			else:	
				if valueList[0]<=valueList[1]:
					result = 1
				else:
					result = 0

	

	if counter == 0:
		(result,errorFlag) = doMath(exp,Line,variables)
		if errorFlag == 1:
			return 0,1
		

	return result,errorFlag

Line = namedtuple('Line', 'line number')
expression = " 2 | 3 "
Line.line = "if (blah) "
Line.number = 1

value = evaluateBooleanExpression(expression, Line, [])
print (value)
	
