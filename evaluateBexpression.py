from collections import namedtuple
from expressionParser import doMath

def evaluateBooleanExpression (expression, Line, variables):
	
	# Check for empty expression
	if not expression:
		print("Error in line " + str(Line.number) + ": " + Line.line)
		print("Description: Invalid boolean expression")
		return 0

	# Call 'evaluateOR' for the expression		
	(value,errorFlag) = evaluateOR(expression,Line,variables)
		
	if (errorFlag == 1):
		return 0
	else:	
		return value
		
	
def evaluateOR (exp,Line,variables):
	# Split by OR	
	expsOR = exp.split("|")

	valueList = []
	# Call 'evaluateAND' for each element of the expsOR list and append the result to 'valueList'
	for eachExp in expsOR:
		if not eachExp:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression")
			return 0, 1
			
		(value,errorFlag) = evaluateAND(eachExp,Line,variables)
		
		if (errorFlag == 1):
			return 0, 1
		else:	
			valueList.append(value)
		
	# Perform OR between elements of the valueList (even when list has only one element) 
	for value in valueList:
		if value != 0:
			return 1, errorFlag
	return 0, errorFlag	


def evaluateAND (exp,Line,variables):
	# Split by AND
	expsAND = exp.split("^") 

	valueList = []
	# Call 'evaluateCondExp' for each element of the expsAND list and append the result to 'valueList'
	for eachExp in expsAND:
		if not eachExp:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression")
			return 0,1
			
		(value,errorFlag) = evaluateCondExp(eachExp,Line,variables)
		
		if (errorFlag == 1):
			return 0, 1
		else:	
			valueList.append(value)

	# Perform AND between elements of valueList (even when list has only one element) 
	for value in valueList:
		if value == 0:
			return 0, errorFlag
	return 1, errorFlag

	
def evaluateCondExp (exp,Line,variables):
	# Check for each possible comparison operator. Check for not operator and send the LHS and RHS to doMath. Throw error if less than 1 or greater than 2 components
	valueList = []
	counter = 0
	if ":eq:" in exp:
		counter = counter+1	
		if counter==2:
			print("Error in line " + str(Line.number) + ": " + Line.line)
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":eq:")
			
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1
				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
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
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":ne:")
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1

				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
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
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":gt:")
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1

				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
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
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":lt:")
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1

				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
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
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":ge:")
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1

				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
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
			print("Description: Invalid boolean expression")
			return 0,1
		else:
			exps = exp.split(":le:")
			for eachExp in exps:
				if not eachExp:
					print("Error in line " + str(Line.number) + ": " + Line.line)
					print("Description: Invalid boolean expression")
					return 0,1

				# Check for NOT
				NOTFlag = 0
				if eachExp[0] == '~':
					eachExp = eachExp[1:]
					NOTFlag = 1
				(errorFlag, value) = doMath(eachExp,Line,variables)
				if errorFlag == 1:
					return 0,1
				else:
					if NOTFlag==1:
						valueList.append(not value)
					else:
						valueList.append(value)
						
			if len(valueList)>2:
				print("Error in line " + str(Line.number) + ": " + Line.line)
				print("Description: Invalid boolean expression")
				return 0,1
			else:	
				if valueList[0]<=valueList[1]:
					result = 1
				else:
					result = 0

	

	if counter == 0:
		(errorFlag,result) = doMath(exp,Line,variables)
		
		if errorFlag == 1:
			return 0,1
		

	return result,errorFlag


