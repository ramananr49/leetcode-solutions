"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

#Below is my code which will work fine for 64 bit not for the above given constrain.
def reverse(x):
    reverse_x = 0
    abs_x = abs(x)
    sign = -1 if x < 0 else 1

    while abs_x > 0:
        digit = abs_x % 10
        reverse_x = (reverse_x * 10) + digit
        abs_x //= 10
        
    reverse_x *= sign
    return reverse_x

print(reverse(123))         #321
print(reverse(-123))        #-321
print(reverse(120))         #21


"""
Below passes the exact Leetcode constrain which is 32 bit
"""
def reverse(x):
    int_max = 2**31-1
    reverse_x = 0
    abs_x = abs(x)
    sign = -1 if x < 0 else 1

    while abs_x > 0:
        digit = abs_x % 10
        if reverse_x > (int_max-digit)//10 :
            return 0
        reverse_x = (reverse_x * 10) + digit
        abs_x //= 10
        
    reverse_x *= sign
    return reverse_x

print(reverse(123))         #321
print(reverse(-123))        #-321
print(reverse(120))         #21
print(reverse(1534236469))  #0