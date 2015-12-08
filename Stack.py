# This file contains the stack ADT

from collections import deque

class Stack:

    # Create a deque
    stack = deque()

    # This function pushes an element onto the stack
    def pushStack(self, newElement):
        self.stack.append(newElement)
        return

    # This function pops the element from the stack
    def popStack(self):

        # Error Flag
        errorFlag = False

        # Check if the stack is empty
        if(len(self.stack)==0):
            errorFlag = True
            return errorFlag, self.stack
        else:
            return errorFlag, self.stack.pop()

    # Checks if the stack is empty
    def isEmpty(self):

        # Check if the length of the stack is empty
        if (len(self.stack)==0):
            return True
        else:
            return False

    # Returns the number of elements in the stack
    def numElements(self):
        return len(self.stack)


    # Returns the first elements of the stack
    def peekStack(self):

        # Error flag
        errorFlag = False

        # Returns the empty stack object if the stack is empty
        if(len(self.stack)==0):
            return errorFlag
        else:
            topElement = self.stack[-1]
            # Return the 'top' element at the end of the deque
            return topElement


