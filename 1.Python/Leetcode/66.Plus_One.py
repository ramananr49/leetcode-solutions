"""
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Example 3:
Input: digits = [9]
Output: [1,0]
"""
digits = [1,2,3]
Output = [1,2,4]
digits1 = [4,3,2,1]
Output1 = [4,3,2,2]
digits2 = [9]
Output2 = [1,0]

def plusOne(digits):
    n = len(digits)
    temp = 0
    if n == 1:
        temp = digits[0]
    else:
        for i in range(n-1, -1, -1):
            temp += digits[i] * (10**(n-i-1))
    plusone = temp+1
    tem = [int(d) for d in str(plusone)]
    return tem
    
print(plusOne(digits))      #[1,2,4]
print(plusOne(digits1))     #[4,3,2,2]
print(plusOne(digits2))     #[1,0]