"""
Problem: 
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:
1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.
If the username is valid then your program should return the string true, otherwise return the string false.

Difficulty: Easy

Approach:

Time Complexity:
Space Complexity:
"""
def CodelandUsernameValidation(word):
    n = len(word)
    if n < 4 or n > 25:
        return False
        
    if not word[0].isalpha():
        return False
            
    if word[-1] == "_":
        return False
        
    if not all(c.isalnum() or c == "_" for c in word):
        return False
    return True

# keep this function call here 
print(CodelandUsernameValidation("aaaaaaaaaa"))  #True
print(CodelandUsernameValidation("__a"))    #False
print(CodelandUsernameValidation("happy_")) #False
print(CodelandUsernameValidation("abc_123")) #True
print(CodelandUsernameValidation("dhgfyudgvbdvhdgfjguhgfdsak"))#False


"""
Notes:
-
-
"""
