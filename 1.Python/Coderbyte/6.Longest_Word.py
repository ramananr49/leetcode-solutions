"""
Have the function LongestWord(sen) take the sen parameter being passed and return 
the longest word in the string. If there are two or more words that are the same length, 
return the first word from the string with that length. Ignore punctuation and assume
 sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

Difficulty: Easy

"""
def LongestWord(sen):
  temp = []

  for word in sen.split():
    if word.isalpha() or word.isdigit():
      temp.append(word)

  return max(temp, key=len)
  

print(LongestWord("I love dogs"))           #love
print(LongestWord("12345 6789 234567"))     #234567
print(LongestWord("fun&!! time"))           #time