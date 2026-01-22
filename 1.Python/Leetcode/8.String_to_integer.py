"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', 
assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character 
is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then round the integer to remain in the range. Specifically, integers less than -231 
should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""

def myAtoi(s):
    int_max = 2**31-1
    int_min = -2**31

    i = 0
    result = 0
    sign = 1
    n = len(s)

    #handle the Whitespace
    while i < n and s[i] == " ":
        i += 1
    
    #handle the sign
    while i < n and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i += 1
    
    #convert digit
    while i < n and s[i].isdigit():
        digit = int(s[i])

        #overflow check
        if result > (int_max-digit)//10:
            if sign == -1:
                return int_min
            else:
                return int_max
        result = (result * 10) + digit
        i += 1

    return result * sign

print(myAtoi("42"))                 #42
print(myAtoi("   -042"))            #-42
print(myAtoi("1337c0d3"))           #1337
print(myAtoi("0-1"))                #0
print(myAtoi("words and 987"))      #0