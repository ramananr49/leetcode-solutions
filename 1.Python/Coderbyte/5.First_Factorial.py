"""
Have the function FirstFactorial(num) take the num parameter being passed and return 
the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
For the test cases, the range will be between 1 and 18 and the input will always be an integer.

Difficulty: Easy

"""
def FirstFactorial(num):
    # 4 * 3 * 2 * 1 = 24
    temp = 1
    while num != 0:
        temp *= num
        num -= 1
    return temp

# keep this function call here 
print(FirstFactorial(4))      #24
print(FirstFactorial(8))      #40320
print(FirstFactorial(5))      #120