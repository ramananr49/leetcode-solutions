"""
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
The sequence looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
How it works:
The first two numbers are defined as 0 and 1.
From the third number onward, each number is the sum of the two previous numbers. For example:
0 + 1 = 1 (the third number),
1 + 1 = 2 (the fourth number),
1 + 2 = 3 (the fifth number),
2 + 3 = 5 (the sixth number), and so on.
"""

def fibonacci(num):
    a = 0
    b = 1
    fibonacci_seq = []

    while a <= num:
        fibonacci_seq.append(a)
        temp = a
        a = b
        b = temp + a

    return fibonacci_seq


print(fibonacci(5))
print(fibonacci(15))
print(fibonacci(25))