"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain 
single digit numbers, letters, and question marks, and check if there are exactly 3 question marks 
between every pair of two numbers that add up to 10. If so, then your program should return 
the string true, otherwise it should return the string false. If there aren't any two numbers 
that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true 
because there are exactly 3 question marks between 6 and 4, and 3 question marks 
between 5 and 5 at the end of the string.

Difficulty: Easy

"""

def QuestionsMarks(word):
    numbers = []
    qmark = []
    
    for i in range(len(word)):
        if word[i].isdigit():
            numbers.append(i)
        if word[i] == "?":
            qmark.append(i)
    found = False
    
    for i in range(len(numbers)):
        idx1 = numbers[i]
        num1 = int(word[idx1])  
        for j in range(i+1, len(numbers)):
            idx2 = numbers[i+1]
            num2 = int(word[idx2])     
            #count ?
            count = 0
            for q in qmark:
                if idx1 < q < idx2:
                    count += 1
            #logic
            if num1 + num2 == 10:
                found = True
                if count != 3:
                    return False
    return found

# keep this function call here 
print(QuestionsMarks("arrb6???4xxbl5???eee5"))      #true
print(QuestionsMarks("aa6?9"))                      #false
print(QuestionsMarks("acc?7??sss?3rr1??????5"))     #true