"""
#write a program to check the given string is Palindrome
"""

def is_palindrome_inbuilt(text):
    return text == text[::-1]

print(is_palindrome_inbuilt("radar"))

def is_palindrome(text):
    res = ""
    for i in range(len(text)-1, -1, -1):
        res += text[i]
    
    return text == res

print(f"The String 'test' is Palindrome :- {is_palindrome("test")}")
print(f"The String 'madam' is Palindrome :- {is_palindrome("madam")}")
print(f"The String 'radar' is Palindrome :- {is_palindrome("radar")}")