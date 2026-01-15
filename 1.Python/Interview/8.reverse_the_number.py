"""
reverse the number
"""

def reverse_num(n):
    temp = 0
    while n != 0:
        last_digit = n % 10
        temp = (temp *10)+last_digit
        n //= 10
    return temp



print(reverse_num(12345))
