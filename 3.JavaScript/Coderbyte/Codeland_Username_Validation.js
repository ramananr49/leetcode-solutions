/*
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
*/

function CodelandUsernameValidation(word)
{
    n = word.length
    
    if (n<4 || n>25) 
    {
        return false
    }
    
    if (!/[a-zA-Z]/.test(word[0]))
    {
        return false
    }
    
    if (word.at(-1) == "_")
    {
        return false
    }
    
    if (!/^[a-zA-Z0-9_]+$/.test(word))
    {
        return false
    }
    
    return true
}


console.log(CodelandUsernameValidation("aaaaaaaaaa"))  //True
console.log(CodelandUsernameValidation("__a"))    //False
console.log(CodelandUsernameValidation("happy_")) //False
console.log(CodelandUsernameValidation("abc_123")) //True
console.log(CodelandUsernameValidation("dhgfyudgvbdvhdgfjguhgfdsak")) //False


/*
Notes:
-
-
*/
