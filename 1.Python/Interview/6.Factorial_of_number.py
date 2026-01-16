"""
#What is a Factorial?
#In mathematics, the factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!.
#n!=n×(n−1)×(n−2)×⋯×1
"""

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

print(factorial(4))     #24
print(factorial(5))     #120
print(factorial(8))     #40320

def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num-1)

print(factorial_recursion(4))
print(factorial_recursion(5))
print(factorial_recursion(8))
