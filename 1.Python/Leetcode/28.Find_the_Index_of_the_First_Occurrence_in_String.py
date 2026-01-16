"""
Given two strings needle and haystack, return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

haystack = "sadbutsad"
needle = "sad"
haystack1 = "leetcode"
needle1 = "leeto"
haystack2 = "goodmorning"
needle2 = "morning"

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        
print(strStr(haystack, needle))     #0
print(strStr(haystack1, needle1))   #-1
print(strStr(haystack2, needle2))   #4