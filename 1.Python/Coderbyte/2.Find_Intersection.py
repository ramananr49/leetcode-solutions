"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr 
which will contain 2 elements: the first element will represent a list of comma-separated 
numbers sorted in ascending order, the second element will represent a second list 
of comma-separated numbers (also sorted). Your goal is to return a comma-separated 
string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Difficulty: Easy

"""

def FindIntersection(strArr):

  set1 = set(map(int, strArr[0].split(", ")))
  set2 = set(map(int, strArr[1].split(", ")))

  set3 = sorted(set1.intersection(set2))

  if set3:
    return ",".join(map(str, set3))
  else:
    return False

# keep this function call here 
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
print(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))
print(FindIntersection(["1, 3, 4", "5, 6, 7"]))