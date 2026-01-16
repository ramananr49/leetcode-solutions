"""
#Write a program to check if two strings are anagrams.
"""

def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)

print(is_anagram("listen", "silent"))


def is_anagram1(text1, text2):
    d1 = {}
    d2 = {}

    if len(text1) != len(text2):
        return False
    
    for c in text1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1

    for e in text1:
        if e not in d2:
            d2[e] = 1
        else:
            d2[e] += 1
    print(d1)
    print(d2)   
    return d1 == d2

print(is_anagram1("listen", "silent"))