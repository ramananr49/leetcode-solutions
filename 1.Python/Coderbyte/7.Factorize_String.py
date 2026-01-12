"""
Write a program to 'factorize' the extremities of two ASCII strings str1+str2

You must return a single string, initially made from the concatenation of two given strings.
The longest substring that is common between the end of the first string and the beginning of the 
the beginning of the second one must be factorized (written only once).

You must decide the concatenation order (str1+str2 or str2+str1) so that you get the best factorization.

when the same number of characters can be factorized by the two concetenation orders, prioritize str1+str2.

Difficulty: Easy

"""
str1 = "1234yyabc"
str2 = "abcxxxx1234"
# output = "1234yyabcxxxx1234"

def factorizeString(text1, text2):
    max_overlap = 0
    min_len = min(len(text1), len(text2))

    for i in range(1, min_len+1):
        if text1[-i:] == text2[:i]:
            max_overlap = i
    
    return text1+text2[max_overlap:]
    
print(factorizeString(str1, str2))     #1234yyabcxxxx1234
print(factorizeString(str2, str1))     #abcxxxx1234yyabc
print(factorizeString("hello", "world")) #helloworld
print(factorizeString("aaaa", "aaab"))  #aaaab