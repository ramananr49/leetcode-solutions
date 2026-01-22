"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

def is_palindrome(st):
    return st == st[::-1]

def longest_palindromic_substring(string):
    n = len(string)
    longest = ""

    for i in range(n):
        for j in range(i, n):
            subtring = string[i:j+1]
            if is_palindrome(subtring):
                if len(subtring) > len(longest):
                    longest = subtring

    return longest

print(longest_palindromic_substring("babad"))       #bab
print(longest_palindromic_substring("abcddcbaef"))  #abcddcba
print(longest_palindromic_substring("aaaabaaa"))    #aaabaaa
print(longest_palindromic_substring("racecar"))     #racecar
print(longest_palindromic_substring("cbbd"))        #bb
print(longest_palindromic_substring("abba"))        #abba