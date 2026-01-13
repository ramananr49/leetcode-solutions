"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
strs_1 = ["flower","flow","flight"]
strs_2 = ["dog","racecar","car"]
strs_3 = ["flow", "flower", "flowing"]
strs_4 = ["a", "ab", "abc"]
strs_5 = ["@home", "@house", "@host"]

def longestCommonPrefix(strs):
    # Check if the input list is empty
    # If empty, there is no common prefix, so return an empty string
    if not strs:
        return ""
        
    # Initialize the prefix as the first string in the list
    # We will try to shorten it if needed
    prefix = strs[0]
    
    # Loop through the remaining strings in the list
    for s in strs[1:]:
        # Keep reducing the prefix until the current string starts with it
        while not s.startswith(prefix):
            # Remove the last character from prefix
            prefix = prefix[:-1]
            # If prefix becomes empty, there is no common prefix
            if prefix == "":
                return ""
    # After checking all strings, return the longest common prefix
    return prefix
    
    
print(longestCommonPrefix(strs_1))   #fl
print(longestCommonPrefix(strs_2))   #""
print(longestCommonPrefix(strs_3))   #flow
print(longestCommonPrefix(strs_4))   #a
print(longestCommonPrefix(strs_5))   #@ho