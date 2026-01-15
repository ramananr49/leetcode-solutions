"""
Write a program to count the occurrences of each character in a string.
"""
from collections import Counter
def char_counter(text):
    return Counter(text)

print(char_counter("Hello"))

chars = Counter("Ramanan")

"""
Write a program to count the occurrences of each character in a string.
#without inbuilt function
"""

def character_count(text):
    d = {}
    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    return d

print(character_count("Hello"))

for k,v in character_count("Hello").items():
    print(f"{k} : {v}")