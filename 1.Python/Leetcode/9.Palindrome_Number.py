"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
x = 121
y = -121
z = 0
a = 10
b = 12321

def isPalindrome(number):
    temp = str(number)
    if temp == temp[::-1]:
        return True
    else:
        return False
    
def isPalindrome(number):
    if number < 0 or (number % 10 == 0 and number != 0):
        return False
    original = number
    rev = 0
    while number > 0:
        digit = number%10
        rev = (rev*10)+digit
        number //= 10
    return rev == original

print(isPalindrome(a))      #False
print(isPalindrome(b))      #True
print(isPalindrome(x))      #True
print(isPalindrome(y))      #False
print(isPalindrome(z))      #True