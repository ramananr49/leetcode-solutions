"""
Have the function FirstReverse(str) take the str parameter being passed and 
return the string in reversed order. For example: if the input string is 
"Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

Difficulty: Easy

"""
def FirstReverse(strParam):

  # code goes here
  return strParam[::-1]

# keep this function call here 
print(FirstReverse("Hello World and Coders"))      #sredoC dna dlroW olleH
print(FirstReverse("coderbyte"))                      #etybredoc
print(FirstReverse("I Love Code"))     #edoC evoL I