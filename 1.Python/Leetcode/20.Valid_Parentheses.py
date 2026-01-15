"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true
"""

def isValid(s):
    # Mapping of closing brackets to opening brackets
    brackets = {")": "(", "]": "[", "}": "{"}      
    # Stack to store opening brackets
    stack = []
     
    # Iterate through each character in the string
    for c in s:        
        # If c is an opening bracket, push it onto the stack
        if c not in brackets:
            stack.append(c)    
        else:
            # If stack is empty, there is no opening bracket to match
            if not stack:
                return False            
            # Pop the top opening bracket from the stack
            popped = stack.pop()    
            # Check if it matches the expected opening bracket
            if popped != brackets[c]:
                return False    
    # At the end, stack must be empty for a valid string
    return not stack


print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("]"))         # False
print(isValid("((("))       # False
print(isValid(""))          # True
